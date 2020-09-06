from __future__ import print_function, unicode_literals

import argparse
import sys

from PyInquirer import prompt

from number_baseball_helper.npc import NPC
from number_baseball_helper.cmd.input_validation import \
    get_guess_number_validator
from number_baseball_helper.cmd import dummy_func


def console_prompt(app: NPC):
    answers = {}
    _questions = [
        {
            "type": "list",
            "name": "command",
            "message": "Select job",
            "choices": [
                {
                    "name": "Think a number",
                    "value": app.think_number.__name__
                },
                {
                    "name": "Try to guess",
                    "value": app.check_number.__name__
                },
                {
                    "name": "Quit",
                    "value": "quit"
                }
            ]
        },
        {
            "type": "input",
            "name": "number_str",
            "message": "What is your guess ? (ex. 1234)",
            "when": lambda answers: answers['command'] ==
                                    app.check_number.__name__,
            "validate": get_guess_number_validator(ndigit=app.ndigit)
        }
    ]
    answers.update(prompt(_questions))
    return answers


def console(app: NPC):
    while True:
        answers = console_prompt(app=app)

        command = answers.pop('command')
        argument = answers

        if command == "quit":
            break

        if hasattr(app, command):
            func = getattr(app, command, dummy_func)
            return_value = func(**argument)
            print(return_value)


def define_get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    parser.add_argument("--ndigit", type=int, default=4)
    parsed = parser.parse_args(argv)
    return parsed


def main(argv=None):
    args = define_get_args(argv)

    npc = NPC(seed=args.seed, ndigit=args.ndigit)
    console(app=npc)


if __name__ == "__main__":
    main(sys.argv[1:])
