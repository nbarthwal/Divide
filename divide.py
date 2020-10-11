from decimal import *
getcontext().prec = 50

B = 10000
N = 15

def div_mod(p):
    r = p % B
    p -= r
    d = int(p / B)
    return d, r


y = [7516, 9784, 2167, 8632]
x = [5736, 2654, 1259, 6221]

n = len(x)
if len(y) == n:
    for i in x:
        if i > B:
            raise Exception('Element in X bigger than base')
    for i in y:
        if i > B:
            raise Exception('Element in Y bigger than base')
else:
    raise Exception('List length not equal')

yy = 0
xx = 0
for i in y:
    yy = B * yy + i
for i in x:
    xx = B * xx + i

print(yy)
print(xx)

print("Ans = ", Decimal(yy)/Decimal(xx))
print('______________________________')

r = [None] * N
for j in range(0, N):
    r[j] = int(B * y[0] / x[0])
    carry = 0
    for i in list(reversed(range(0, n))):
        (carry, y[i]) = div_mod(carry + B * y[i] - r[j] * x[i])
    y[0] += B*carry

carry = 0
for j in list(reversed(range(1, N))):
    (carry, r[j]) = div_mod(carry + r[j])
r[0] += carry
print(r)

