"""
CPE101
Spring 2021
Author: Jack Forrester
"""

def max_of_two(x, y):
    """Finds the largest of two given integers
    Args:
         x: the number to be compared to y
         y: the number to be compared to x
    Returns:
         The larger of x and y
    Examples:
         >>> max_of_two(6, 9)
         9
         >>> max_of_two(77, 46)
         77
         >>> max_of_two(50, 50)
         50
    """
    if x > y:
        print(x)
    else:
        print(y)

def max_of_three(x, y, z):
    """Finds the largest of three given integers
    Args:
         x: the number to be compared to y and z
         y: the number to be compared to x and z
         z: the number to be compared to x and y
    Returns:
         The largest of x, y and z
    Examples:
         >>> max_of_three(9, 1, 5)
         9
         >>> max_of_three(20, 22, 13)
         22
         >>> max_of_three(76, 109, 334)
         334
    """
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

def mul(x, y):
    """Finds the product of two given integers
    Args:
         x: the number to be multiplied by y
         y: the number to be multiplied by x
    Return:
         p: The product of x and y
    Examples:
         >>> mul(33, 99)
         3267
         >>> mul(18, 9)
         162
         >>> mul(42, 42)
         1764
    """
    i = 1
    p = x 
    while i < y:
        p += x
        i += 1
    if x == 0 or y == 0:
        return 0
    else:
        return p

def exp(x, y):
    """Finds the value of the first given integer to the power of the second given integer
    Args:
         x: the numer to be exponentiated
         y: the exponent
    Returns:
         e: the value of x raised to the power of y
    Examples:
         >>> exp(2, 4)
         16
         >>> exp(33, 3)
         35937
         >>> exp(23, 6)
         148035889
    """
    i = 1
    e = x
    while i < y:
        e = mul(e, x)
        i += 1
    if y == 0:
        return 1
    else:
        return e

if __name__ == '__main__':
    import doctest
    doctest.testmod()
