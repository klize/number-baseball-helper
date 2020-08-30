class Case(tuple):
    def __new__(cls, strike, ball, ndigit):
        assert strike + ball <= ndigit
        return tuple.__new__(cls, (strike, ball))



