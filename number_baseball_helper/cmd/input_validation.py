from prompt_toolkit.validation import Validator, ValidationError

import regex


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
