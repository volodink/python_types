# Тип tuple

a = 1
b = 2
print(a, b)

temp = a
a = b
b = temp
a, b = b, a
print(a, b)

# chart point -> x y
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# chart point -> (x, y)
points = [e for e in zip(x, y)]
print(f'points = {points}')

for x_e, y_e in zip(x, y):
    print(f'x:{x_e}\t\ty:{y_e}')

s1 = [1,2,3,4,5,6]
s1[1] = 'qwe'
print(s1)

s = 'qweqweqe'[:]
print(s)
s[0] = 'Q'
print(s)
