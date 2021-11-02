from main import *

def test_to_check_if_year_is_divisible_by_4_but_not_100():
    assert True == isLeapYear(2024)

def test_to_check_if_year_is_divisible_by_400():
    assert True == isLeapYear(2000)
    assert True == isLeapYear(1570)

def test_to_check_if_year_is_not_divisible_by_4():
    assert True != isLeapYear(1705)

def test_to_check_if_year_is_not_divisible_by_100_but_not400():
    assert True != isLeapYear(1900)

