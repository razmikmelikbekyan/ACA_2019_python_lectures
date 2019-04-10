a = 1
print(type(a))

b = 1.2
print(type(b))

c = 6 + 4j
print(type(c))

a = 7 + 8j
print(type(a))

b = "hello"
print(b)
print(type(b))

a = 10
b = 25

c = a + b
print(c)
print(type(c))

c = a - b
print(c)
print(type(c))

c = a * b
print(c)
print(type(c))

c = b / a
print(c)
print(type(c))

c = 5 / 5
print(c)
print(type(c))

c = b // a
print(c)
print(type(c))

c = b % a
print(c)
print(type(c))

c = 5 ** 2
print(c)
print(type(c))

c = a * -1.
print(c)
print(type(c))

from decimal import Decimal

a = Decimal('2')
print(a)
print(type(a))

b = Decimal('3')
print(b)
print(type(b))

c = a + b
print(c)
print(type(c))

a = int('4')
print(a)

a = 12.3
b = 23.5

c = a == b
print(c)
print(type(c))

c = a != b
print(c)
print(type(c))

c = Decimal('12') == 12.0
print(c)
print(type(c))

c = 2.555555555 / 10.0
print(c)
print(type(c))
print(Decimal(str(c)))

c = Decimal('2.555555555') / Decimal('10.0')
print(c)
print(type(c))

a = 5
b = 7.8
print(a > b)

print(a >= b)
print(a < b)
print(a <= b)

c = 1.1 + 2.2
tol = 1e-8

dif = abs(c - 3.3) <= tol
print(dif)

print(type(dif))

print(dif * 17)

a = 5
b = 10
c = 25

check = a > b and c > b





