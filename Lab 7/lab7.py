"""
CPE101
Spring 2021
Author: Jack Forrester
"""


import math


def square_all(int_list: list) -> list:
    """Creates a new list whose elements are the square of each value of the
    given list
    Args:
        int_list (list): a list consisting of only integers
    Returns:
        a new list whose elements are the square of each value in int_list
    Examples:
        >>> square_all([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> square_all(list([10, 6, 9]))
        [100, 36, 81]
        >>> square_all([22])
        [484]
    """

    return [num ** 2 for num in int_list]


def add_n_all(int_list: list, num: int) -> list:
    """Creates a new list with num added to each element of the given list
    Args:
        int_list (list): a list consisting of only integers
        num (int): the number to be added to each element of int_list
    Returns:
        a new list with num added to each element of int_list
    Examples:
        >>> add_n_all([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 6, 7]
        >>> add_n_all(list([10, 6, 9]), 10)
        [20, 16, 19]
        >>> add_n_all([22], 22)
        [44]
    """

    result = []
    size = len(int_list)
    init = 0
    while init < size:
        new = int_list[init] + num
        result.append(new)
        init += 1
    return result


def is_even_all(int_list: list) -> list:
    """Creates a new list containing boolean values representing whether each
    corresponding integer in the given list is even (True) or odd (False)
    Args:
        int_list (list): a list consisting of only integers
    Returns:
        a new list whose elements are the boolean values of each corresponding
        integer in int_list
    Examples:
        >>> is_even_all([1, 2, 3, 4, 5])
        [False, True, False, True, False]
        >>> is_even_all(list([10, 6, 9]))
        [True, True, False]
        >>> is_even_all([22])
        [True]
    """

    result = []
    for num in int_list:
        result.append(num % 2 == 0)
    return result


def are_positive(int_list: list) -> list:
    """Creates a new list containing all positive values of the given list
    Args:
        int_list (list): a list consisting of only integers
    Returns:
        a new list whose elements are only the positive values in int_list
    Examples:
        >>> are_positive([1, -2, 3, 4, -5])
        [1, 3, 4]
        >>> are_positive(list([-10, 6, -9]))
        [6]
        >>> are_positive([-22])
        []
    """

    return [num for num in int_list if num > 0]


def are_greater_than_n(int_list: list, num: int) -> list:
    """Creates a new list of all integers in the given list that are greater
    than num
    Args:
        int_list (list): a list consisting of only integers
        num (int): the number which acts as the parameter for filtering
    Returns:
        a new list whose elements are the values in int_list greater than num
    Examples:
        >>> are_greater_than_n([1, 2, 3, 4, 5], 2)
        [3, 4, 5]
        >>> are_greater_than_n(list([10, 6, 9]), 7)
        [10, 9]
        >>> are_greater_than_n([22], 22)
        []
    """

    result = []
    size = len(int_list)
    init = 0
    while init < size:
        if int_list[init] > num:
            result.append(int_list[init])
            init += 1
        else:
            init += 1
    return result


def are_divisible_by_n(int_list: list, num: int) -> list:
    """Creates a new list of all integers in the given list that are divisible
    by num
    Args:
        int_list (list): a list consisting of only integers
        num (int): the number which acts as the parameter for filtering
    Returns:
        a new list whose elements are the values in int_list divisible by num
    Examples:
        >>> are_divisible_by_n([1, 2, 3, 4, 5], 2)
        [2, 4]
        >>> are_divisible_by_n(list([10, 6, 0, 9]), 3)
        [6, 0, 9]
        >>> are_divisible_by_n([22], 22)
        [22]
    """

    result = []
    for init in int_list:
        if init % num == 0:
            result.append(init)
    return result


def my_avg(my_list: list) -> float:
    """Finds the average value of all integers in the given list
    Args:
        my_list (list): a list consisting of only integers
    Returns:
        the average value of all the integers in my_list
    Examples:
        >>> my_avg([1, -2, 3, 4, -5])
        0.2
        >>> my_avg(list([-10, 6, 0, -9]))
        -3.25
        >>> my_avg([-22])
        -22.0
    """

    accum = 0
    size = len(my_list)
    for num in my_list:
        accum += num
    return accum / size


def index_of_smallest(my_list: list) -> int:
    """Finds the index of the smallest value in the given list
    Args:
        my_list (list): a list consisting of only integers
    Returns:
        the index of the first occurance of the smallest value in my_list,
        -1 if empty
    Examples:
        >>> index_of_smallest([1, -2, 3, 4, -5])
        4
        >>> index_of_smallest([-10, 6, 0, -9])
        0
        >>> index_of_smallest([])
        -1
    """

    size = len(my_list)
    if size == 0:
        index = -1
    else:
        current_min = my_list[0]
        init = 0
        index = 0
        while init < size:
            if my_list[init] < current_min:
                current_min = my_list[init]
                index = init
                init += 1
            else:
                init += 1
    return index


def pascal_triangle(dim: int) -> list:
    """Generates a Pascal Triangle
    Args:
        dim (int): number of rows of the Pascal Triangle
    Returns:
        A n x n matrix which represents a triangular array of the binomial
        coefficients
    Examples:
        >>> expected1 = [[1.0, 0, 0, 0], [1.0, 1.0, 0, 0], [1.0, 2.0, 1.0, 0],
        ... [1.0, 3.0, 3.0, 1.0]]
        >>> pascal_triangle(4) == expected1
        True
        >>> expected2 = [[1.0, 0, 0, 0, 0, 0], [1.0, 1.0, 0, 0, 0, 0],
        ... [1.0, 2.0, 1.0, 0, 0, 0], [1.0, 3.0, 3.0, 1.0, 0, 0],
        ... [1.0, 4.0, 6.0, 4.0, 1.0, 0], [1.0, 5.0, 10.0, 10.0, 5.0, 1.0]]
        >>> pascal_triangle(6) == expected2
        True
        >>> expected3 = [[1.0, 0], [1.0, 1.0]]
        >>> pascal_triangle(2) == expected3
        True
    """

    matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(0)
        matrix.append(row)
    for i in range(1, dim+1):
        for j in range(1, i+1):
            matrix[i-1][j-1] = \
            math.factorial(i-1)/(math.factorial(j-1)*math.factorial(i-j))
    return matrix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
