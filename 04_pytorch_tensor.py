# Tensor 개념

import torch

tensor1 = torch.tensor([[[1.,2.],[3.,4.]],[[5.,6.],[7.,8.]]])
print(tensor1)
# tensor([[[1., 2.],
#          [3., 4.]],

#         [[5., 6.],
#          [7., 8.]]])

tensor2 = torch.tensor([[[9.,10.],[11.,12.]],[[13.,14.],[15.,16.]]])
print(tensor2)
# tensor([[[ 9., 10.],
#          [11., 12.]],

#         [[13., 14.],
#          [15., 16.]]])


# 텐서 사칙연산 가능

add_tensor = tensor1 + tensor2
print(add_tensor)
# tensor([[[10., 12.],
#          [14., 16.]],

#         [[18., 20.],
#          [22., 24.]]])

sub_tensor = tensor1 - tensor2
print(sub_tensor)
# tensor([[[-8., -8.],
#          [-8., -8.]],

#         [[-8., -8.],
#          [-8., -8.]]])

mul_tensor = tensor1 * tensor2
print(mul_tensor)
# tensor([[[  9.,  20.],
#          [ 33.,  48.]],

#         [[ 65.,  84.],
#          [105., 128.]]])

div_tensor = tensor1 / tensor2
print(div_tensor)
# tensor([[[0.1111, 0.2000],
#          [0.2727, 0.3333]],

#         [[0.3846, 0.4286],
#          [0.4667, 0.5000]]])


# torch  모듈에 내장된 메서드 이용해서도 가능

torch.add(tensor1, tensor2) 
# tensor([[[10., 12.],
#          [14., 16.]],

#         [[18., 20.],
#          [22., 24.]]])
torch.sub(tensor1,tensor2)
# tensor([[[-8., -8.],
#          [-8., -8.]],

#         [[-8., -8.],
#          [-8., -8.]]])
torch.mul(tensor1, tensor2)
# tensor([[[  9.,  20.],
#          [ 33.,  48.]],

#         [[ 65.,  84.],
#          [105., 128.]]])
torch.div(tensor1, tensor2)
# tensor([[[0.1111, 0.2000],
#          [0.2727, 0.3333]],

#         [[0.3846, 0.4286],
#          [0.4667, 0.5000]]])

# 행렬 곱 연산
torch.matmul(tensor1, tensor2)
# tensor([[[ 31.,  34.],
#          [ 71.,  78.]],

#         [[155., 166.],
#          [211., 226.]]])
