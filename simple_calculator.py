a=float (input("Enter first number: "))
b=float (input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':      
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"
print("Result:", result)
print("Thank you for playing!") 