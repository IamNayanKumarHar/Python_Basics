a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = int(input("Enter value of d: "))

result1 = a + b * c ** d

result2 = (a + b) * c // d

result3 = a // b + a % b * c ** d

result4 = (a > b) and (c < d) or (a != b)

result5 = (a & b) | (c ^ d)

result6 = (a << 2) + (b >> 1)

print("Expression 1:", result1)
print("Expression 2:", result2)
print("Expression 3:", result3)
print("Expression 4:", result4)
print("Expression 5:", result5)
print("Expression 6:", result6)