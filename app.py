# Call function from
from utils.pythagors import hypotenuse

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
