class Case(tuple):
    def __new__(cls, strike, ball, ndigit):
        assert strike + ball <= ndigit
        return tuple.__new__(cls, (strike, ball))

    def __str__(self):
        return f"{self[0]} strike {self[1]} ball"


_case_to_name = {}
_name_to_case = {}


def _make_case_to_name(ndigit: int):
    cton = {}
    for strike in range(ndigit):
        possible_balls_cnt = ndigit - strike
        if possible_balls_cnt == 1:
            possible_balls = range(possible_balls_cnt)
        else:
            possible_balls = range(possible_balls_cnt + 1)

        for ball in possible_balls:
            case = Case(strike, ball, ndigit)
            name = f"{strike} strike {ball} ball"

            cton.update({case: name})
    return cton


def case_to_name(ndigit: int):
    return _make_case_to_name(ndigit) if _case_to_name == {} else _case_to_name

