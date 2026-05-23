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

#tensor random

random_tensor=torch.rand(3,3)

print(random_tensor)

#Tensor operation
x1=torch.tensor([1,2,3])
x2=torch.tensor([4,5,6])
#add
print(x1+x2)
# print(torch.add(x1,x2))
# #subtract
# print(x1-x2)
# print(torch.subtract(x1,x2))
# #multiply
# print(x1*x2)
# print(torch.multiply(x1,x2))
# #divide
# print(x1/x2)
# print(torch.divide(x1,x2))
# #dot product
# print(torch.dot(x1,x2))

# #matrix multiplication
# x1=torch.tensor([[1,2],[3,4]])
# x2=torch.tensor([[5,6],[7,8]])  