# Matrix 개념

import torch

matrix1 = torch.tensor([[1.,2.],[3.,4.]])
print(matrix1)
# tensor([[1., 2.],
#         [3., 4.]])

matrix2 = torch.tensor([[5.,6.],[7.,8.]])
print(matrix2)
# tensor([[5., 6.],
#         [7., 8.]])


# 백터 사칙연산 가능

add_matrix = matrix1 + matrix2
print(add_matrix)
# tensor([[ 6.,  8.],
#         [10., 12.]])

sub_matrix = matrix1 - matrix2
print(sub_matrix)
# tensor([[-4., -4.],
#         [-4., -4.]])

mul_matrix = matrix1 * matrix2
print(mul_matrix)
# tensor([[ 5., 12.],
#         [21., 32.]])

div_matrix = matrix1 / matrix2
print(div_matrix)
# tensor([[0.2000, 0.3333],
#         [0.4286, 0.5000]])


# torch  모듈에 내장된 메서드 이용해서도 가능

torch.add(matrix1, matrix2) 
# tensor([[ 6.,  8.],
#         [10., 12.]])
torch.sub(matrix1,matrix2)
# tensor([[-4., -4.],
#         [-4., -4.]])
torch.mul(matrix1, matrix2)
# tensor([[ 5., 12.],
#         [21., 32.]])
torch.div(matrix1, matrix2)
# tensor([[0.2000, 0.3333],
#         [0.4286, 0.5000]])

# 행렬 곱 연산
torch.matmul(matrix1, matrix2)
# tensor([[19., 22.],
#         [43., 50.]])
