import formulas
import pytest


#### quadratic() ####
def test_quadratic_zero_solutions():
    assert formulas.quadratic(4.00,6.00,9.00) == 0

def test_quadratic_one_solutions():
    assert formulas.quadratic(1.00,-8.00,16.00) == 1

def test_quadratic_two_solutions():
    assert formulas.quadratic(2.00,4.50,2.00) == 2


#### comp_interest() ####


#### cont_comp_interest() ####


#### varriable_in_exp() ####
