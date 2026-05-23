import torch
import torch.nn as nn

model=nn.Sequential(
    nn.Linear(784,10),
    nn.ReLU(),
    nn.Linear(10,5)
)
x=torch.rand(1,784)

output=model(x)
print(output)
print(output.shape)
