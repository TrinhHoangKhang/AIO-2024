import pytest
import math
from unittest.mock import patch
import sys
import os
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Homework/Week1')))
import activation_function as af

def test_is_number_with_number():
    assert af.is_number('3.14') == True

def test_is_number_with_non_number():
    assert af.is_number('abc') == False

def test_sigmoid_with_positive_number():
    x = 1
    expected_output = 1 / (1 + math.exp(-x))
    assert af.sigmoid(x) == expected_output

def test_sigmoid_with_negative_number():
    x = -1
    expected_output = 1 / (1 + math.exp(-x))
    assert af.sigmoid(x) == expected_output

def test_relu_with_positive_number():
    x = 1
    expected_output = 1
    assert af.relu(x) == expected_output

def test_relu_with_negative_number():
    x = -1
    expected_output = 0
    assert af.relu(x) == expected_output

def test_relu_with_zero():
    x = 0
    expected_output = 0
    assert af.relu(x) == expected_output

def test_elu_with_positive_number():
    x = 1
    expected_output = 1
    assert af.elu(x) == expected_output

def test_elu_with_negative_number():
    x = -1
    alpha = 0.01
    expected_output = alpha * (math.exp(x) - 1)
    assert af.elu(x) == pytest.approx(expected_output)

def test_elu_with_zero():
    x = 0
    alpha = 0.01
    expected_output = alpha * (math.exp(x) - 1)
    assert af.elu(x) == pytest.approx(expected_output)
