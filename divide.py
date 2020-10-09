B = 1000


def div_mod(p):
    r = p % B
    p -= r
    d = int(p / B)
    return d, r


y = [984, 217, 632]
x = [254, 129, 621]

if len(y) == len(x):
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
k = int(B * y[0]/x[0])

print("K = ", k)
print("Ans = ", yy/xx)
diff = (yy*B - xx * k)
print(diff)
print('______________________________')
carry = 0
y.append(0)
y.reverse()
x.reverse()

for i in range(0, len(x)):
    z = carry - (x[i]*k)
    (dz, rz) = div_mod(z)
    new_y = rz + y[i]

    print(dz, rz, new_y)

    #(dz, dr) = div_mod(z)
    #set(y, i, dr)
    #carry = dz + dx

    print(i, carry, y)
    #(carry, z) = div_mod(carry + y[i+1] - k*x[i])
    #y[i+1] = z

# carry = carry + y[0]
#del y[0]
# print(0, carry, y)


