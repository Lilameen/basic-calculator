
# Get two numbers from the user
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print("Addition (x + y):", x + y)

print("Subtraction (x - y):", x - y)

# my code checks if y is not zero to avoid errors... 
if y != 0:
    print("Division (x / y):", x / y)
else:
    print("error!")