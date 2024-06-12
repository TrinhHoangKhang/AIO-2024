import math

message = 'n must be a positive integer'


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def approx_sin(x, n):
    '''
    This function computes approximate value of sin(x) 

    '''
    # Check
    if not isinstance(n, int) or n <= 0:
        print(message)
        return

    # Compute
    result = 0
    for i in range(0, n):
        result += (-1)**i * (x**(2*i + 1)) / factorial(2*i + 1)

    print(result)


def approx_cos(x, n):
    '''
    This function computes approximate value of cos(x) 

    '''
    # Check
    if not isinstance(n, int) or n <= 0:
        print(message)
        return

    # Compute
    result = 0
    for i in range(0, n):
        result += (-1)**i * (x**(2*i)) / factorial(2*i)

    print(result)


def approx_sinh(x, n):
    '''
    This function computes approximate value of sinh(x) 

    '''
    # Check
    if not isinstance(n, int) or n <= 0:
        print(message)
        return

    # Compute
    result = 0
    for i in range(0, n):
        result += (x**(2*i + 1)) / factorial(2*i + 1)

    print(result)


def approx_cosh(x, n):
    '''
    This function computes approximate value of sin(x) 

    '''
    # Check
    if not isinstance(n, int) or n <= 0:
        print(message)
        return

    # Compute
    result = 0
    for i in range(0, n):
        result += (x**(2*i)) / factorial(2*i)

    print(result)


# Test
if __name__ == '__main__':
    x = 3.14
    n = 10
    approx_sin(x, n)

    print('-------------------')
    approx_cos(x, n)

    print('-------------------')
    approx_sinh(x, n)

    print('-------------------')
    approx_cosh(x, n)
