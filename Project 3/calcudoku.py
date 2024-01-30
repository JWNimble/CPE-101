"""
CPE101
Spring 2021
Author: Jack Forrester
"""


def get_num_cages():
    """Obtains the number of cages
    Returns:
        int: the number of cages
    """

    while True:
        cage_total = input('Enter the number of cages: ')
        if cage_total.isalpha():
            print(cage_total, "is not an integer!")
        elif cage_total.isdigit():
            cage_total_int = int(cage_total)
            if 1 <= cage_total_int <= 25:
                break
        print("That is not a valid value")
    return int(cage_total)


def get_cage_info(num):
    """Obtains information regarding the cages and converts the given
    information into a usable list of lists
    Args:
        num (int): the number of cages
    Returns:
        list: a list of lists containing integers regarding information about
        the cages
    """

    cage_info = []
    i = 0
    while i < num:
        input_cage = input('Enter information about a cage: ')
        cage_str_list = input_cage.split()
        cage_int_list = [int(i) for i in cage_str_list]
        cage_info.append(cage_int_list)
        i += 1
    return cage_info

def validate_rows(grid):
    """Checks if any row in the grid contains duplicate positive numbers
    Args:
        grid (list): a 2D list of integers representing the cells of the puzzle
    Returns:
        True if all rows contain no duplicate positive numbers, False otherwise
    """

    row_validate = []
    for row in grid:
        row_check = [num for num in row if num == 0 or row.count(num) == 1]
        if len(row_check) == len(grid[0]):
            row_validate.append(row_check)
    return len(row_validate) == len(grid)

def transpose_grid(grid) -> list:
    """Transposes a grid
    Args:
        grid (list): a grid
    Returns:
        list: a list of lists which is a transposed version of the grid
    """

    return [[row[column] for row in grid] for column in range(len(grid[0]))]


def validate_cols(grid):
    """Checks if any column in the grid contains duplicate positive numbers
    Args:
        grid (list): a 2D list of integers representing the cells of the puzzle
    Returns:
        True if all columns contain no duplicate positive numbers,
        False otherwise
    """
    tp_grid = transpose_grid(grid)
    col_validate = []
    for col in tp_grid:
        col_check = [num for num in col if num == 0 or col.count(num) == 1]
        if len(col_check) == len(grid[0]):
            col_validate.append(col_check)
    return len(col_validate) == len(grid)


def validate_cages(grid, cages):
    """Checks if the sum of the values in any partially populated cage equals
    or exceeds the required sum
    Args:
        grid (list): a 2D list of integers representing the cells of the puzzle
        cages (list): a 2D list of integers representing the values read from
        input
    Returns:
        True if the sum of values in a fully populated cage equals the required
        sum or the sum of values in a partially populated cage is less than the
        required sum, False otherwise
    """

    dim = len(grid)
    cage_check = []
    for cage in cages:
        accum = 0
        if len(cage) >= 3:
            pos = None
            for pos in cage[2:]:
                accum += grid[pos // dim][pos % dim]
            if accum < cage[0] and grid[pos // dim].count(0) > 0:
                cage_check.append(accum)
            elif accum == cage[0]:
                cage_check.append(accum)
    return len(cage_check) == len(cages)


def validate_all(grid, cages):
    """Checks if the puzzle is in a valid state
    Args:
        grid (list): a 2D list of integers representing the cells of the puzzle
        cages (list): a 2D list of integers representing the values read from
        input
    Returns:
        True if all three validation functions return True, False otherwise
    """
    row_check = validate_rows(grid)
    col_check = validate_cols(grid)
    cage_check = validate_cages(grid, cages)
    return row_check and col_check and cage_check


def create_grid(dim):
    """Creates a grid of dim * dim
    Args:
        dim (int): the dimension
    Returns:
        list: a list of lists of 0s
    """

    matrix = []
    i = 0
    while i < dim:
        row = []
        i += 1
        j = 0
        while j < dim:
            row.append(0)
            j += 1
        matrix.append(row)
    return matrix


def print_grid(grid):
    """Prints the grid.
    Args:
        grid (list): a list of lists
    """

    for row in grid:
        print(*row, sep=' ')


def main():
    """Executes an exhaustive search algorithm for the input cage information
    """
    cage_num = get_num_cages()
    cage_info = get_cage_info(cage_num)
    grid = create_grid(5)
    column = 0
    row = 0
    while row < 5:
        grid[row][column] += 1
        if validate_all(grid, cage_info):
            column += 1
            if column == 5:
                column = 0
                row += 1
        elif grid[row][column] == 5:
            while grid[row][column] == 5:
                grid[row][column] = 0
                column -= 1
                if column < 0:
                    column = 4
                    row -= 1
    print_grid(grid)


if __name__ == '__main__':
    main()
