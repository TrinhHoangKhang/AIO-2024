import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def compute_activation_function():
    '''
    This function computues the activation function value at x
    Available activation functions: sigmoid, relu, elu
    
    '''
    # get x
    print('Input x = ', end='')
    x = input()

    # Check
    if not is_number(x):
        print('x must be a number')
        return

    # Get activation function
    print('Input activation Function (sigmoid|relu|elu): ', end = '')
    activation_function = input()

    # Check
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_function} is not supported')
        return
    
    # Compute
    x = float(x)
    if activation_function == 'sigmoid':
        print(f'sigmoid: f({x}) = {sigmoid(x)}')
    elif activation_function == 'relu':
        print(f'relu: f({x}) = {relu(x)}')
    else:
        print(f'elu: f({x}) = {elu(x)}')

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    if x <= 0: return 0
    return x

def elu(x, alpha = 0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    return x

# Test 
if __name__ == '__main__':
    compute_activation_function()