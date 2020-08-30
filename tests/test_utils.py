import pytest

from itertools import permutations
from number_baseball_helper.utils import generate_number_strings


@pytest.mark.parametrize('ndigit', (4, 5, 6))
def test_generate_number_strings(ndigit):
    candidates = [i for i in generate_number_strings(ndigit)]
    assert len(candidates) == len(list(permutations([i for i in range(10)],
                                                    ndigit)))
