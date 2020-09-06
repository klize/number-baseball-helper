import random

from number_baseball_helper.case import Case
from number_baseball_helper.utils import check_case


class NPC:
    def __init__(self, seed=None, ndigit: int = 4):
        self._seed = seed
        self._ndigit = ndigit

        random.seed(a=seed)

        self._number_str = None

    @property
    def ndigit(self):
        return self._ndigit

    def _think_number(self):
        number = random.randrange(0, 10 ** self._ndigit)
        number_str = f"{number:0{self._ndigit}d}"
        return number_str

    def think_number(self):
        number_str = self._think_number()
        while len(set(number_str)) != self._ndigit:
            number_str = self._think_number()

        self._number_str = number_str

    def check_number(self, number_str: str):
        case = check_case(self._number_str, number_str, self._ndigit)
        if case == Case(self._ndigit, 0, self._ndigit):
            return "found"
        return case

    def start_console(self):
        self.think_number()

        while True:
            a = input(">> ")

            if a == "q":
                break

            if len(a) != self._ndigit or len(set(a)) != self._ndigit:
                print("wrong input")
                continue

            result = self.check_number(a)

            if result == (self._ndigit, 0):
                print(f"{result} strike {self._number_str}")
                break
            else:
                print(f"{result[0]} strike {result[1]} ball")
