from fixture_learning import sample_name,bonus,sample_salary

def test_something(sample_name):
    assert sample_name=="dhruva"


def test_salary_fix(sample_salary):
    result=bonus(sample_salary,5)
    assert result == 1250

def test_negative_salary():
    import pytest
    with pytest.raises(ValueError):
        bonus(-20000,5)