from addition import add
from division import div
from multiplication import mul
from subtraction import sub
from modulus import mod

# 입력
a, b = map(int, input().split())

# 출력
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(mod(a,b))

