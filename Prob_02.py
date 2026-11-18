num = int(input("Enter a five-digit number: "))

d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10

digit_sum = d1+d2+d3+d4+d5
digit_product = d1*d2*d3*d4*d5

reverse = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1

difference = num - reverse

print("First Digit:", d1)
print("Second Digit:", d2)
print("Third Digit:", d3)
print("Fourth Digit:", d4)
print("Fifth Digit:", d5)
print("Sum of Digits:", digit_sum)
print("Product of Digits:", digit_product)
print("Reversed Number:", reverse)
print("Difference:", difference)
print("Middle Digit:", d3)