"""
Tests for assignment_One.py
"""
import assignment_One as ao
import pytest


def test_calculate_distance():
    coord1 = [0,0,2]
    coord2 = [0,0,0]

    observed = ao.calculate_distance(coord1, coord2)
    assert observed == 2.0

def test_bond_check_false():
    """
    A test for bond_check function.
    """
    bond_length = 3.0

    observed = ao.bond_check(bond_length)
    assert observed == False


def test_bond_check_true():
    """
    A test for bond_check function.
    """
    bond_length = 1.4

    observed = ao.bond_check(bond_length)
    assert observed == True

def test_bond_check_error():
    bond_length='a'
    with pytest.raises(TypeError):
        observed = ao.bond_check(bond_length)
