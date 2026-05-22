"""testing calc function"""
import pytest
from app import add
def test_add_positive():
    """test for positive"""
    assert add(2, 3) == 5

def test_add_negative():
    """test for negative"""
    assert add(-1, -1) == -2

def test_add_zero():
    """test for zero"""
    assert add(0, 0) == 0

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (1, 1, 2),
        (5, 5, 10)
    ]
)
def test_add(a, b, result):
    """test with parameters"""
    assert a + b == result
