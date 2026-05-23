import torch

x=torch.tensor([1,2,3,4,5,6,7,80,9,10])

print(x)
print(x.dtype)
print(x.shape)

#example
#scaler
a=torch.tensor(5)

#vector
vector=torch.tensor([2,3,4,5,6,7,8,9])

#matrix

matrix=torch.tensor([
    [1,2,3],
    [4,5,6],
    [7,8,9]

])

print(a)
print(vector)
print(matrix)

Tensor_shape=torch.tensor([
    [1,2,3,5,5],
    [4,5,6,5,5],
    [7,8,9,5,5]
])

print(Tensor_shape.shape)
