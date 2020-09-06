from number_baseball_helper.case import Case
from number_baseball_helper.helper import Candidate


def test_scan_candidate(helper_class):
    helper = helper_class(ndigit=4)
    candidates = helper.candidates[:6] + helper.candidates[5040-5:]
    answer_number_str = candidates[5].number_str
    guess_number_str = candidates[4].number_str
    result = Case(0, 2, ndigit=4)

    helper.scan_candidate(guess_number_str, result)

    actual_candidates = helper.candidates[:6] + helper.candidates[5040-5:]

    expected_candidates = [
        Candidate("0123").false(),
        Candidate("0124").false(),
        Candidate("0125").false(),
        Candidate("0126").false(),
        Candidate("0127").false(),
        Candidate("0128").false(),
        Candidate("9872"),
        Candidate("9873").false(),
        Candidate("9874").false(),
        Candidate("9875").false(),
        Candidate("9876").false(),
    ]

    for ac, ec in zip(actual_candidates, expected_candidates):
        assert ac.number_str == ec.number_str
        assert ac._is_candidate == ec._is_candidate
