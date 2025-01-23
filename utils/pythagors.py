# Write a code to calulate hypotenuse take input from users
def hypotenuse(a: int | float, b: int | float) -> float:
    """
    This function calculates hypotenuse for given sides
    of a right angled triangle
    """
    return (a**2 + b**2) ** (1 / 2)
