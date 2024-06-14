import os
import sys
import pytest
import math
import builtins
from io import StringIO


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Homework/Week1')))
import activation_function as af

def test_compute_activation_function():
    assert af.compute_activation_function(0, 'relu') == None

def test_is_number():
    assert af.is_number(1) == True


def test_sigmoid():
    assert math.isclose(af.sigmoid(0), 0.5, rel_tol=1e-9)


def test_relu():
    assert af.relu(0) == 0


def test_elu():
    assert af.elu(0) == 0
