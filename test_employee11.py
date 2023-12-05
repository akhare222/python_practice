import pytest
from Employee11 import Employee

@pytest.fixture
def employee():
    return Employee('Aditi', 'Khare', 1_000_000)

def test_give_default_raise(employee):
    salary = employee.annual_salary
    assert salary == 1_000_000

def test_give_custom_raise(employee):
    salary = employee.give_raise(1)
    assert salary == 1_000_001

