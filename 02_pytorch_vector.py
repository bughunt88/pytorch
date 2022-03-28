# Vector 개념

import torch

vector1 = torch.tensor([1.,2.,3.])
print(vector1)
# tensor([1., 2., 3.])

vector2 = torch.tensor([4.,5.,6.])
print(vector2)
# tensor([4., 5., 6.])


# 백터 사칙연산 가능

add_vector = vector1 + vector2
print(add_vector)
# tensor([5., 7., 9.])

sub_vector = vector1 - vector2
print(sub_vector)
# tensor([-3., -3., -3.])

mul_vector = vector1 * vector2
print(mul_vector)
# tensor([ 4., 10., 18.])

div_vector = vector1 / vector2
print(div_vector)
# tensor([0.2500, 0.4000, 0.5000])



# torch  모듈에 내장된 메서드 이용해서도 가능

torch.add(vector1, vector2) 
# tensor([5., 7., 9.])
torch.sub(vector1,vector2)
# tensor([-3., -3., -3.])
torch.mul(vector1, vector2)
# tensor([ 4., 10., 18.])
torch.div(vector1, vector2)
# tensor([0.2500, 0.4000, 0.5000])

# 내적 연산
torch.dot(vector1, vector2)
# tensor(32.)
