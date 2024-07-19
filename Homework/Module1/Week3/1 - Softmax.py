import torch
import torch.nn as nn
import torch.nn.functional as F

'''
This is a simple implementation of the softmax function using PyTorch.

'''
class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=0)


'''
This is a simple implementation of the softmax stable function using PyTorch.

'''
class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_stable = x - torch.max(x)
        return torch.exp(x_stable) / torch.sum(torch.exp(x_stable), dim=0)


# Test
data = torch . Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch . Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
