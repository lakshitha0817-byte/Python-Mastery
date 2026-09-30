num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

temp = num1
num1 = num2
num2 = temp


print("After swapping:")
print("first number =", num1)
print("second number =", num2)