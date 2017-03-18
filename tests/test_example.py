""" Test example """
import pybaseline
from pybaseline.__main__ import main


def test_example():
    """ Example test """
    assert pybaseline.example_function(42) == 42


def test_main_arg():
    """ Test main uses arguments """
    assert main(['--expected_result', '35']) == 35


def test_main_no_arg():
    """ Test main uses defaults """
    assert main([]) == 7
