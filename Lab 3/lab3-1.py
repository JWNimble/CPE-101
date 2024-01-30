"""
CPE101
Spring 2021
Author: Jack Forrester
"""

def print_hello():
    """Asks the user for thier name and prints hello + name"""
    name = input("Enter your name: ")
    return print("Hello", name)

def get_numbers():
    """Asks the user to input two number and prints the sum"""
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    c = x + y
    return c

def cube(num:int)->int:
    """Cubes the num. This is a Google-style docstring.

    Args:
         num (int): The number to be cubed.

    Returns:
         int: The cubed number.

    Examples:
         >>> cube(1)
         1
         >>> cube(2)
         8
         >>> cube(3)
         27
    """

    return num ** 3
     
def get_hypotenuse(a:float, b:float)->float:
    """Find the hypotenuse of a right triangle by using the lengths of its sides
    
    Args:
         a (float): The length of one of the triangle's sides
         b (float): The length of the other of the triangle's sides
    
    Returns:
         float: the triangle's hypotenuse by using pythagorean theorum, the square root of one side squared plus the other squared

    Examples:
         >>> get_hypotenuse(1, 2)
         2.23606797749979
         >>> get_hypotenuse(3, 5)
         5.830951894845301
         >>> get_hypotenuse(10, 13)
         16.401219466856727
    """

    return ((a ** 2) + (b ** 2)) ** (1/2)

def do_math(x:float, y:float)->float:
    """Finds the solution to a math function given the selcted x and y values

    Args:
         x (float): x value
         y (float): y value

    Returns:
         float: The solution to the math problem 3 time x squared plus 4 times y all divided by 2 times x

    Examples:
         >>> do_math(2, 3)
         6.0
         >>> do_math(5, 7)
         10.3
         >>> do_math(11, 35)
         22.863636363636363
    """

    return ((3 * (x ** 2)) + (4 * y)) / (2 * x)

def is_positive(num:int)->bool:
    """

    Args:
         num (int): The number to be tested for being positive or negetive

    Return:
         bool: True if positive, False otherwise

    Examples:
         >>> is_positive(2)
         True
         >>> is_positive(-3)
         False
         >>> is_positive(368)
         True
    """

    return num > 0

def both_positive(num1:int, num2:int)->bool:
    """Find if both numbers are positive

    Args:
         num1 (int): The first number to be tested for positivity
         num2 (int): The second number to be tested for positivity

    Returns:
         bool: True if both are positive, False otherwise

    Examples:
         >>> both_positive(2, 8)
         True
         >>> both_positive(13, -22)
         False
         >>> both_positive(-33, -33)
         False
    """

    return is_positive(num1) == True and is_positive(num2) == True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print_hello()
    sum_numbers = get_numbers()
    print(sum_numbers)
