import pytest

from add_num import add


# 全局应用
@pytest.fixture
def result():
    return 3


def test_add2(result):
    sum = add(1, 2)
    assert sum == result


def test_add3(result):
    sum = add(2, 1)
    assert sum == result
