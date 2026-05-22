from app import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (1, 1, 2),
        (5, 5, 10)
    ]
)
def test_add(a, b, result):
    assert a + b == result