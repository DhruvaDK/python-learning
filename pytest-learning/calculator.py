def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError ("b cannot be 0")
    return a/b

def bonus(salary,percent):
    if salary < 0:
        raise ValueError("salary cannot be zero")
    return salary * percent / 100


### using fixture here 

import pytest

@pytest.fixture
def engineer_data():
    return {"name":"DHRUVA","age":24}

@pytest.fixture
def sample_salary():
    return 25000