import pytest

from number_baseball_helper.helper import NumberBaseballHelper


@pytest.fixture()
def helper_class():
    return NumberBaseballHelper
