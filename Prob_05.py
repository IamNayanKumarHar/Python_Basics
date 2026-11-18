input1 = input("Enter Input 1: ")
input2 = input("Enter Input 2: ")
input3 = input("Enter Input 3: ")

print("\n--- Original Values and Types ---")

print("Input 1:", input1, "Type:", type(input1))
print("Input 2:", input2, "Type:", type(input2))
print("Input 3:", input3, "Type:", type(input3))

num1 = int(input1)
num2 = float(input2)
num3 = str(input3)

print("\n--- Converted Values and Types ---")

print("First Value:", num1, "Type:", type(num1))
print("Second Value:", num2, "Type:", type(num2))
print("Third Value:", num3, "Type:", type(num3))

number3 = int(input3)

total = num1 + num2 + number3

average = total / 3

maximum = max(num1, num2, number3)

minimum = min(num1, num2, number3)

square = num1 ** 2

cube = number3 ** 3

print("\n--- Numeric Operations ---")

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Square of First Number:", square)
print("Cube of Third Number:", cube)

condition1 = num1 > num2

condition2 = total % 5 == 0

condition3 = 10 <= average <= 100

condition4 = num1 > 0 and num2 > 0 and number3 > 0

print("\n--- Boolean Analysis ---")

print("First Number Greater Than Second:", condition1)
print("Sum Divisible By 5:", condition2)
print("Average Between 10 and 100:", condition3)
print("All Numbers Are Positive:", condition4)

print("\n--- Final Results ---")

print("Original Values:", input1, input2, input3)
print("Converted Values:", num1, num2, num3)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Square:", square)
print("Cube:", cube)

print("Boolean Results:", condition1, condition2, condition3, condition4)