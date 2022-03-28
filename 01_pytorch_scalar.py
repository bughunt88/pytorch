# scalar 개념

import torch

scalar1 = torch.tensor([1.])
print(scalar1)
# tensor([1.])

scalar2 = torch.tensor([3.])
print(scalar2)
# tensor([3.])


# 스칼라 사칙연산 가능

add_scalar = scalar1 + scalar2
print(add_scalar)
# tensor([4.])

sub_scaler = scalar1 - scalar2
print(sub_scaler)
# tensor([-2.])

mul_scalar = scalar1 * scalar2
print(mul_scalar)
# tensor([3.])

div_scalar = scalar1 / scalar2
print(div_scalar)
# tensor([0.3333])


# torch  모듈에 내장된 메서드 이용해서도 가능

torch.add(scalar1, scalar2) 
# tensor([4.])
torch.sub(scalar1,scalar2)
# tensor([-2.])
torch.mul(scalar1, scalar2)
# tensor([3.])
torch.div(scalar1, scalar2)
# tensor([0.3333])
