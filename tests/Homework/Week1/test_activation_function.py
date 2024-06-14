import pytest
import math
from unittest.mock import patch
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Homework/Week1')))
import activation_function as af

def test_is_number_valid():
    assert af.is_number('1') == True

def test_is_number_invalid():
    assert af.is_number('abc') == False

def test_sigmoid():
    assert math.isclose(af.sigmoid(0), 0.5, rel_tol=1e-9)

def test_relu_positive():
    assert af.relu(5) == 5

def test_relu_zero():
    assert af.relu(0) == 0

def test_relu_negative():
    assert af.relu(-5) == 0

def test_elu_positive():
    assert af.elu(5) == 5

def test_elu_zero():
    assert af.elu(0) == 0

def test_elu_negative():
    assert af.elu(-5) == -0.9950041652780257