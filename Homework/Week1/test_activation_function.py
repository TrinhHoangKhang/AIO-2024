import pytest
import math
from unittest.mock import patch
import sys
import os
from io import StringIO

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Homework/Week1')))
import activation_function as af

def test_is_number():
    assert af.is_number('3.14') == True

def test_sigmoid():
    x = 1
    expected_output = 1 / (1 + math.exp(-x))
    assert af.sigmoid(x) == expected_output

def test_relu():
    x = 1
    expected_output = 1
    assert af.relu(x) == expected_output

def test_elu():
    x = 1
    expected_output = 1
    assert af.elu(x) == expected_output
