"""Test example."""
from mock import patch
import sys
import pybaseline
from pybaseline.__main__ import main


def test_example():
    """Example test."""
    assert pybaseline.example_function(42) == 42


def test_main_arg():
    """Test main uses arguments."""
    sys_args = ['exe.exe', '--expected_result', '35']
    with patch.object(sys, 'argv', sys_args):
        assert main() == 35


def test_main_no_arg():
    """Test main uses defaults."""
    sys_args = ['exe.exe']
    with patch.object(sys, 'argv', sys_args):
        assert main() == 7
