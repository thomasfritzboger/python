import calculate
import pytest
from math import isclose

def test_square():
    assert calculate.square(5) == 25
    assert calculate.square(-1) == 1
    assert calculate.square(0) == 0
    assert calculate.square(-1.5) == 2.25

def test_sqrt():
    assert calculate.sqrt(16) == 4
    assert isclose(calculate.sqrt(0.5), 0.707106, rel_tol=1e-5)

