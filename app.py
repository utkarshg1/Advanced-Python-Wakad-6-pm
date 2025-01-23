# Write a code to calulate hypotenuse take input from users
def hypotenuse(a: int|float , b: int|float) -> float:
    """
    This function calculates hypotenuse for given sides
    of a right angled triangle
    """
    return (a**2 + b**2)**(1/2)

# Take input from user
a = float(input("Please enter side a : "))
b = float(input("Please enter side b : "))

# Calculate and print hypotenuse
c = hypotenuse(a, b)

# Print
print(f"Hypotenuse of sides {a} and {b} is {c:.4f}")

# View > Terminal
# Make sure you open cmd
# Write in terminal - python app.py
