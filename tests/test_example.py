""" Test example """
import pybaseline
import pybaseline.main


def test_example():
    """ Example test """
    assert pybaseline.example_function(42) == 42


def test_main_arg():
    """ Test main uses arguments """
    assert pybaseline.main.main(['--expected_result', '35']) == 35


def test_main_no_arg():
    """ Test main uses defaults """
    assert pybaseline.main.main([]) == 7
