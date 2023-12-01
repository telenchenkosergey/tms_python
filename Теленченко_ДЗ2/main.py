divider = '-' * 20

# Задание 1
a, b, c = 3, 3, 3
print(id(a))
print(id(b))
print(id(c))
print(divider)

# Задание 2
x = [4, 5]
y = [4, 5]
print(id(x))
print(id(y))
print(divider)

# Задание 3
b = float(b)
c = str(c)
x = tuple(x)
y = x
print(id(a))
print(id(b))
print(id(c))
print(id(x))
print(id(y))
print(divider)
