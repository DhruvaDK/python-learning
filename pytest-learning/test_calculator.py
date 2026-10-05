from calculator import add,subtract,multiply,divide,bonus,engineer_data,sample_salary

def test_add():
    result=add(3,4)
    assert result == 7

def test_subtract():
    result=subtract(10,5)
    assert result == 5

def test_multiply():
    result=multiply(10,20)
    assert result== 200

def test_divide():
    result=divide(10,5)
    assert result== 2
def test_bonus():
    result=bonus(20000,5)
    assert result == 1000

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10,0)

def test_add_negative():
    result=add(-3,-4)
    assert result == -7

def test_something(engineer_data):
    assert engineer_data["name"]=="DHRUVA"

def test_something(engineer_data):
    assert engineer_data["age"]==24

def test_salary_fix(sample_salary):
    result=bonus(sample_salary,5)
    assert result == 1250

def test_negative_salary():
    import pytest
    with pytest.raises(ValueError):
        bonus(-20000,5)