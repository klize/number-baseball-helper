class Case(tuple):
    def __new__(cls, strike, ball, ndigit):
        assert strike + ball <= ndigit
        return tuple.__new__(cls, (strike, ball))


_case_to_name = {}
_name_to_case = {}


def make_cases(ndigit: int):
    global _case_to_name
    global _name_to_case

    _case_to_name = _make_case_to_name(ndigit)
    _name_to_case = _make_name_to_case(ndigit)


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


def _make_name_to_case(ndigit: int):
    pass


def case_to_name(ndigit: int):
    return _make_case_to_name(ndigit) if _case_to_name == {} else _case_to_name

