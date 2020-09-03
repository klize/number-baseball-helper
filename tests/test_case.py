import pytest

from number_baseball_helper.case import Case, case_to_name


@pytest.mark.parametrize('ndigit', (4, 5, 6))
def test_case_to_name(ndigit):
    assert len(case_to_name(ndigit)) == (ndigit + 1) * (ndigit + 2) / 2 - 2