"""
CPE101
Spring 2021
Author: Jack Forrester
"""


import sys


def main_helper(infile_idx: int)->list:
    """Counts each kind of value read from a given file and find the sum of the
    numbers
    Args:
        infile_idx (int): the index of the file to be read
    Returns:
        list: a list containg values for the number total, other total, and sum
    """

    argval = sys.argv
    num = 0
    other = 0
    num_sum = 0
    with open(argval[infile_idx], 'r') as inf:
        inf_c = inf.readlines()
        for line in inf_c:
            v_list = line.split()
            for value in v_list:
                try:
                    int_test = int(value)
                    if isinstance(int_test, int):
                        num += 1
                        num_sum += int_test
                except:
                    other += 1
    return [num, other, num_sum]


def main():
    """Executes the main_helper function and writes the results into a new
    file by a given name.
    """

    argval = sys.argv
    if len(argval) == 3:
        try:
            output = main_helper(1)
            with open(argval[2], 'w') as outf:
                outf.write('numbers: %d\n' % output[0])
                outf.write('other: %d\n' % output[1])
        except IOError:
            infile_name = argval[1]
            print(f"Unable to open {infile_name}")
    elif len(argval) == 4:
        if argval[1] == '-s':
            try:
                output = main_helper(2)
                with open(argval[3], 'w') as outf:
                    outf.write('numbers: %d\n' % output[0])
                    outf.write('other: %d\n' % output[1])
                    outf.write('sum: %d\n' % output[2])
            except IOError:
                infile_name = argval[2]
                print(f"Unable to open {infile_name}")
        elif argval[3] == '-s':
            try:
                output = main_helper(1)
                with open(argval[2], 'w') as outf:
                    outf.write('numbers: %d\n' % output[0])
                    outf.write('other: %d\n' % output[1])
                    outf.write('sum: %d\n' % output[2])
            except IOError:
                infile_name = argval[1]
                print(f"Unable to open {infile_name}")
        else:
            print("Usage: [-s] infile_name outfile_name [-s]")
    else:
        print("Usage: [-s] infile_name outfile_name [-s]")


if __name__ == '__main__':
    main()
