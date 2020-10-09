B = 1000
N = 5

def div_mod(p):
    r = p % B
    p -= r
    d = int(p / B)
    return d, r


y = [456, 984, 217, 632]
x = [176, 254, 129, 621]

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

print("Ans = ", yy*1.0/xx*1.0)
print('______________________________')

r = [None] * N
for j in range(0, N):
    r[j] = int(B * y[0] / x[0])
    carry = 0
    for i in list(reversed(range(0, n))):
        (carry, y[i]) = div_mod(carry + B * y[i] - r[j] * x[i])
    y[0] += B*carry

carry = 0
for j in list(reversed(range(0, N))):
    (carry, r[j]) = div_mod(carry + r[j])
r[0] += carry * B
print(r)
