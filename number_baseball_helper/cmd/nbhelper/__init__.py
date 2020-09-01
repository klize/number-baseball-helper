from __future__ import print_function, unicode_literals

import argparse
import sys
import regex

from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

from number_baseball_helper.case import Case, case_to_name
from number_baseball_helper.helper import NumberBaseballHelper


class PropertyMixIn:
    def __init__(self, property_name, property_value):
        setattr(self, property_name, property_value)


def get_guess_number_validator(ndigit: int):
    class GuessNumberValidator(Validator):
        _ndigit = ndigit

        def validate(self, document):
            ndigit_regex = "^\\d{" + f"{self._ndigit}" + "}$"
            ok = regex.match(
                ndigit_regex,
                document.text)
            if not ok:
                raise ValidationError(
                    message='Please enter a valid guess number string',
                    cursor_position=len(document.text))

    return GuessNumberValidator


def console_prompt(app: NumberBaseballHelper):
    answers = {}
    _questions = [
        {
            "type": "list",
            "name": "command",
            "message": "Select job",
            "choices": [
                {
                    "name": "Scan candidates",
                    "value": app.scan_candidate.__name__
                },
                {
                    "name": "Show candidates",
                    "value": app.show_candidate.__name__
                },
                {
                    "name": "Pick a random candidate",
                    "value": app.choose_next_guess.__name__
                },
                {
                    "name": "Quit",
                    "value": "quit"
                }
            ]
        },
        {
            "type": "input",
            "name": "guess_number_str",
            "message": "What is your guess ? (ex. 1234)",
            "when": lambda answers: answers['command'] ==
                                    app.scan_candidate.__name__,
            "validate": get_guess_number_validator(ndigit=app.ndigit)
        },
        {
            "type": "list",
            "name": "result",
            "message": "Of which case is your last guess ?",
            "when": lambda answers: answers['command'] ==
                                    app.scan_candidate.__name__,
            "choices": [
                {
                    "name": name,
                    "value": case
                } for case, name in case_to_name(app.ndigit).items()
            ]
        }
    ]
    answers.update(prompt(_questions))
    return answers


def console(app: NumberBaseballHelper):
    while True:
        answers = console_prompt(app=app)
        print(answers)

        command = answers.pop('command')
        argument = answers

        if command == "quit":
            break

        if hasattr(app, command):
            func = getattr(app, command, dummy_func)
            return_value = func(**argument)
            print(return_value)


def dummy_func():
    yield


def define_get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ndigit", type=int, default=4)
    parsed = parser.parse_args(argv)
    return parsed


def main(argv=None):
    args = define_get_args(argv)

    helper = NumberBaseballHelper(ndigit=args.ndigit)
    # helper.start_console()
    console(app=helper)


if __name__ == "__main__":
    main(sys.argv[1:])
