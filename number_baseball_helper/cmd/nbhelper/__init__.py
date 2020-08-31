from __future__ import print_function, unicode_literals

import argparse
import sys

from PyInquirer import prompt

from number_baseball_helper.helper import NumberBaseballHelper


def console(app: NumberBaseballHelper):
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
                "Pick a random candidate",
                {
                    "name": "test",
                    "value": 1
                },
                "Quit"
            ]
        },
        {
            "type": "list",
            "name": "argument",
            "message": "Of which case is your last guess ?",
            "when": lambda answers: answers['command'] ==
                                    app.scan_candidate.__name__
            "choices": [
                {
                    "name": "3 Strike"
                }
            ]

        }
    ]
    answers = prompt(_questions)
    return answers


def define_get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ndigit", type=int, default=4)
    parsed = parser.parse_args(argv)
    return parsed


def main(argv=None):
    args = define_get_args(argv)

    helper = NumberBaseballHelper(ndigit=args.ndigit)
    # helper.start_console()
    print(answers)

if __name__ == "__main__":
    main(sys.argv[1:])
