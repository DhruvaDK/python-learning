from calculator import add,multiply,bonus

import pytest

@pytest.mark.parametrize("a,b,expected",[(2,4,6),(-1,-2,-3)])

def test_add(a,b,expected):
    assert add(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[(2,3,6),(4,10,40)])

def test_multiply(a,b,expected):
    assert multiply(a,b)==expected


