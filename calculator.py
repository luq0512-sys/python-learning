# Calculator 1

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number"))

operation = input("Choose (+, -, *, /):")

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    print("Result:", num1 / num2)

elif num2 == 0:
    print("Cannot divide by zero!")

else:
    print("Invalid operation!")



