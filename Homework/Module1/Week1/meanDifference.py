import math


def md_nre_single_sample(y, y_hat, n, p):
    '''
    This function compute md_nre for given y, y_hat, n, p

    '''
    print(math.pow(math.pow(y, 1/n) - math.pow(y_hat, 1/n), p))


# Test
if __name__ == '__main__':
    md_nre_single_sample(100, 99.5, 2, 1)
    md_nre_single_sample(50, 49.5, 2, 1)
    md_nre_single_sample(20, 19.5, 2, 1)
    md_nre_single_sample(0.6, 0.1, 2, 1)
