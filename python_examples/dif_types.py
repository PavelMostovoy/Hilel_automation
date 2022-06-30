import fractions
from decimal import Decimal

print(1 + 2)
print("a" + "b")
var = 1 + 1.1

print(type(var))

print(10 / 3)

a = Decimal("0.1")
b = Decimal("0.1")
c = Decimal("0.1")
d = a + b + c
e = Decimal("0.3")

print(d)
print(e == d)

fract = fractions.Fraction(1, 3)
print(fract, fract*3)


a = 1
b = 1
c = 1
d = a + b + c
e = 3

print(e == d)


a = 0.1
b = 0.1
c = 0.1
d = a + b + c
e = 0.3

print(d)
print(e == d)