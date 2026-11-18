a = 10
b = 20
c = 30

a = a + b
b = a - b
a = a - b

b, c = c, b

d = a + b + c
e = d / 3

result = d > e * 2

print("a =", a, "Type:", type(a))
print("b =", b, "Type:", type(b))
print("c =", c, "Type:", type(c))
print("d =", d, "Type:", type(d))
print("e =", e, "Type:", type(e))
print("Condition:", result)
print("Type:", type(result))