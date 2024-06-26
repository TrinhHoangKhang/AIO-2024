import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def get_inputs():
    '''
    This function gets and validates the inputs from the user
    '''

    # get x
    print('Input x = ', end='')
    x = input()

    # Check
    if not is_number(x):
        print('x must be a number')
        return None, None

    # Get activation function
    print('Input activation Function (sigmoid|relu|elu): ', end='')
    activation_function = input()

    # Check
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_function} is not supported')
        return None, None

    return float(x), activation_function


def compute_activation_function(x=None, activation_function=None):
    '''
    This function computes the activation function value at x
    Available activation functions: sigmoid, relu, elu
    '''

    if x is None or activation_function is None:
        x, activation_function = get_inputs()

    # Compute
    if activation_function == 'sigmoid':
        print(f'sigmoid: f({x}) = {sigmoid(x)}')
    elif activation_function == 'relu':
        print(f'relu: f({x}) = {relu(x)}')
    else:
        print(f'elu: f({x}) = {elu(x)}')


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    return x


def elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    return x
