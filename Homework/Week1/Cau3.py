import math
import random

def compute_loss():
    # Get number of samples
    print('Input number of samples (integer number) which are generated: ', end='')
    n = input()

    # Check
    if not n.isnumeric():
        print('number of samples must be an integer number')
        return
    
    n = int(n)

    # Get loss name
    print('Input loss name ', end = '')
    loss = input()

    # Check
    if loss not in ['MSE', 'MAE', 'RMSE']:
        print(f'{loss} is not supported')
        return
    
    # Compute
    finalLoss = 0
    for i in range (0, n):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss == 'MAE':
            lossValue = math.fabs(target - pred)
        elif (loss == 'MSE') or (loss == 'RMSE'):
            lossValue = math.pow(target - pred, 2)

        finalLoss += lossValue
        print(f'loss name: {loss}, sample: {i}, pred: {pred}, target: {target}, loss: {lossValue}')

    if loss == 'MAE':
        finalLoss /= n
    elif loss == 'MSE':
        finalLoss /= n
    elif loss == 'RMSE':
        finalLoss = math.sqrt(finalLoss / n)

    print(f'final {loss}: {finalLoss}')


# Test
if __name__ == '__main__':
    compute_loss()
    
