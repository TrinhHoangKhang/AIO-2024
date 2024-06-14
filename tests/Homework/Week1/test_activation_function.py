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

@patch('builtins.input', side_effect=['5', 'sigmoid'])
def test_get_inputs_valid(mock_input):
    x, activation_function = af.get_inputs()
    assert x == 5.0
    assert activation_function == 'sigmoid'

@patch('builtins.input', side_effect=['abc', 'sigmoid'])
def test_get_inputs_invalid_x(mock_input):
    x, activation_function = af.get_inputs()
    assert x == None
    assert activation_function == None

@patch('builtins.input', side_effect=['5', 'invalid'])
def test_get_inputs_invalid_activation(mock_input):
    x, activation_function = af.get_inputs()
    assert x == None
    assert activation_function == None

@patch('sys.stdout', new_callable=StringIO)
@patch('builtins.input', side_effect=['5', 'sigmoid'])
def test_compute_activation_function_stdout(mock_input, mock_stdout):
    af.compute_activation_function()
    output = mock_stdout.getvalue().strip()
    assert output.startswith('sigmoid: f(5.0) =')