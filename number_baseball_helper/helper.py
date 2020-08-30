import random

from number_baseball_helper.utils import generate_number_strings, check_case
from number_baseball_helper.case import Case


class NumberBaseballHelper:
    def __init__(self, ndigit: int = 4):
        self._ndigit = ndigit
        self.candidates = []

        self._num_candidates = self.init_candidates(self._ndigit)

    @property
    def ndigit(self):
        return self._ndigit

    def init_candidates(self, ndigit: int = 4) -> int:
        self._ndigit = ndigit
        self.candidates = [Candidate(number_string) for number_string in
                           generate_number_strings(self._ndigit)]
        return len(self.candidates)

    def guess(self, number_str) -> Case:
        # TODO: check number_str input
        raise NotImplementedError("coming soon")

    def scan_candidate(self, guess_number_str, result: Case):
        first_true_candidate_index = -1
        for index, candidate in enumerate(self.candidates):
            if result != candidate.check(guess_number_str):
                candidate.false()
                self._num_candidates -= 1
            else:
                if first_true_candidate_index < 0:
                    first_true_candidate_index = index
        return first_true_candidate_index

    def show_candidate(self):
        return list(filter(None, self.candidates))

    def choose_next_guess(self):
        return random.choice(self.show_candidate())

    def start_console(self):
        while True:
            a = input("[guess] [strike] [ball]>> ").split(" ")

            if a[0] == "q":
                break

            if a[0] == "show":
                print(self.show_candidate())
                continue

            if a[0] == "choice":
                print(self.choose_next_guess())
                continue

            if len(a) != 3 or len(a[0]) != self._ndigit or len(set(a[0])) != \
                    self._ndigit:
                print("wrong input")
                continue

            guess_number_str = a[0]
            strike, ball = map(int, a[1:])
            result = Case(strike, ball, ndigit=self.ndigit)
            self.scan_candidate(guess_number_str, result)


class Candidate:
    def __init__(self, number_str):
        # TODO: number_str ndigit check
        self._number_str = number_str
        self._is_candidate = True

    @property
    def number_str(self):
        return self._number_str

    def __repr__(self):
        return self._number_str

    def __bool__(self):
        return self._is_candidate

    def true(self):
        self._is_candidate = True
        return self

    def false(self):
        self._is_candidate = False
        return self

    def check(self, guess_number_str):
        return check_case(self._number_str,
                          guess_number_str,
                          len(self._number_str))
