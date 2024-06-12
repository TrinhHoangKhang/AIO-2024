import math
import random


def compute_loss():
    '''
    This function computes loss value 
    Available loss functions: MSE, MAE, RMSE

    '''
    # Get number of samples
    print('Input number of samples (integer number) which are generated: ', end='')
    n = input()

    # Check
    if not n.isnumeric():
        print('number of samples must be an integer number')
        return

    n = int(n)

    # Get loss name
    print('Input loss name ', end='')
    loss = input()

    # Check
    if loss not in ['MSE', 'MAE', 'RMSE']:
        print(f'{loss} is not supported')
        return

    # Compute
    final_loss = 0
    for i in range(0, n):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss == 'MAE':
            loss_value = math.fabs(target - pred)
        elif (loss == 'MSE') or (loss == 'RMSE'):
            loss_value = math.pow(target - pred, 2)

        final_loss += loss_value
        print(
            f'loss name: {loss}, sample: {i}, pred: {pred}, target: {target}, loss: {loss_value}')

    if loss == 'MAE':
        final_loss /= n
    elif loss == 'MSE':
        final_loss /= n
    elif loss == 'RMSE':
        final_loss = math.sqrt(final_loss / n)

    print(f'final {loss}: {finalLoss}')


# Test
if __name__ == '__main__':
    compute_loss()
