import pytest
@pytest.fixture
def sample_name():
    return "dhruva"



def bonus(salary,percent):
    if salary < 0:
        raise ValueError("salary cannot be zero")
    return salary * percent / 100

@pytest.fixture
def sample_salary():
    return 25000
    