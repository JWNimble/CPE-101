"""
Project 4

CPE101
Spring 2021
Author: Jack Forrester
"""


import sys
from copy import copy


class Crime:
    """Stores data read from crimes.tsv and times.tsv
    Attributes:
        crime_id (int): ID number representing the specific crime
        category (str): the type of crime
        day_of_week (str): day of week when the crime took place
        month (str): month when the crime took place
        hour (str): hour when the crime took place
    """

    def __init__(self, crime_id: int, category: str):
        """The initializer for a crime object
        Args:
            crime_id (int): crime ID number
            category: type of crime
        """

        self.crime_id = int(crime_id)
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None


    def __eq__(self, other):
        return isinstance(other, Crime) and \
                    self.crime_id == other.crime_id and \
                    self.category == other.category and \
                    self.day_of_week == other.day_of_week and \
                    self.month == other.month and self.hour == other.hour


    def __repr__(self):
        return f"{self.crime_id}\t{self.category}\t{self.day_of_week}\t"\
                + f"{self.month}\t{self.hour}\n"


def create_crimes(lines: list)->list:
    """Creates a list of crime objects without duplicates
    Args:
        lines (list): a list of strings rpresenting lines from crimes.tsv
    Returns:
        list: a list of crime objects for each unique robbery
    """

    crimes = []
    ids = []
    for line in lines:
        elements = line.strip().split('\t')
        id_ = int(elements[0])
        if elements[1] == 'ROBBERY' and id_ not in ids:
            crimes.append(Crime(id_, elements[1]))
            ids.append(id_)
    return crimes


def sort_crimes(crimes: list)->list:
    """Sorts a list of crime objects by ID number using insertion sort method
    Args:
        crimes (list): a list of crime objects
    Returns:
        list: a list of crime objects sorted by thier ID number
    """

    sortc = copy(crimes)
    size = len(sortc)
    for i in range(1, size):
        j = i
        while j > 0 and sortc[j-1].crime_id > sortc[j].crime_id:
            sortc[j-1].crime_id, sortc[j].crime_id = \
                    sortc[j].crime_id, sortc[j-1].crime_id
            j -= 1
    return sortc


def set_crimetime(crime: Crime, day_of_week: str, month: int, hour: int)->None:
    """Updates the day_of_week, month, and hour attributes of the crime onject
    Args:
        crime (Crime): a crime object
        day_of_week (str): a string containing a day of the week
        month (int): month attribute represented by an integer between 1 and 12
        hour (int): hour attribute represented by an integer between 0 and 23
    Returns:
        an updated crime object with the month and hour attributes transformed
        to thier appropriate string representations
    """

    crime.day_of_week = day_of_week
    months = [None, 'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
    crime.month = months[month]
    amh = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM',
            '9AM', '10AM', '11AM']
    pmh = ['12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM',
            '9PM', '10PM', '11PM']
    if hour < 12:
        crime.hour = amh[hour]
    else:
        crime.hour = pmh[hour - 12]


def update_crimes(crimes: list, lines: list)->None:
    """Updates the attributes of the crime objects in a given list
    Args:
        crimes (list): a list of crime objects sorted by ID number
        lines (list): a list of strings representing lines from times.tsv
    Returns:
        a list of crime objects with updated attributes
    """

    for line in lines:
        attr = line.strip().split('\t')
        dow = attr[1]
        date = attr[2]
        month = date[0:2]
        time = attr[3]
        hour = time[0:2]
        crime_idx = find_crime(crimes, int(attr[0]))
        if crime_idx != -1:
            crime = crimes[crime_idx]
            set_crimetime(crime, dow, int(month), int(hour))


def find_crime(crimes: list, crime_id: int)->int:
    """Finds the position of a crime object with a given crime ID number
    in a list of sorted crime objects by using a binary search method
    Args:
        crimes (list): a list of crime objects sorted by ID number
        crime_id (int): the id number of the crime object to be located
    Returns:
        int: the index of the crime object with the given id number,
        -1 if not found
    """

    low, high = 0, len(crimes) - 1
    while low <= high:
        mid = (high + low) // 2
        if crimes[mid].crime_id < crime_id:
            low = mid + 1
        elif crimes[mid].crime_id > crime_id:
            high = mid - 1
        else:
            return mid
    return -1


def how_many(lst: list, element)->int:
    """Counts the number of occurences of an element in a list
    Args:
        lst (list): a list
        element: the element which will be counted
    Returns:
        int: an integer representing the number of occurrences of the given
        element in the given list
    """

    count = 0
    for ele in lst:
        if ele == element:
            count = count + 1
    return count


def max_rob_by_attr(crimes: list, attribute: str)->str:
    """Finds the most frequent element in terms of robberies for a specified
    attribute of a crime object
    Args:
        crimes (list): a list of crime objects sorted by ID number
        attribute (str): an attribute of the crime object
    Returns:
        str: the element with the most robberies for the given attribute
    """

    attr_list = []
    for crime in crimes:
        if attribute == 'day_of_week':
            attr_list.append(crime.day_of_week)
        elif attribute == 'month':
            attr_list.append(crime.month)
        elif attribute == 'hour':
            attr_list.append(crime.hour)
    counter = 0
    most = attr_list[0]
    for attr in attr_list:
        freq = how_many(attr_list, attr)
        if freq > counter:
            counter = freq
            most = attr
    return most


def main():
    """Reads information from the the files specified in the first and second
    command-line arguments and writes data combined from the provided files
    for crimes catagorized as a robbery in a new file whose name is specified
    by the third command-line argument. Also displays the total number of
    processed robberies and the day of the week, month, and hour with the
    most robberies
    """

    argval = sys.argv
    if len(argval) == 4:
        try:
            with open(argval[1], 'r') as cfile, open(argval[2], 'r') as tfile:
                crime_lines = cfile.readlines()
                times = tfile.readlines()
        except IOError:
            print('Unable to open one or both of the files provided')
        else:
            try:
                crime_lines.remove(crime_lines[0])
                times.remove(times[0])
                crimes = create_crimes(crime_lines)
                crime_sort = sort_crimes(crimes)
                update_crimes(crime_sort, times)
                day_most = max_rob_by_attr(crime_sort, 'day_of_week')
                month_most = max_rob_by_attr(crime_sort, 'month')
                hour_most = max_rob_by_attr(crime_sort, 'hour')
                rob_sum = len(crime_sort)
                str_crimes = ''.join([str(var) for var in crime_sort])
                with open(argval[3], 'w') as robberies:
                    robberies.write('ID\tCategory\tDayOfWeek\tMonth\tHour\n')
                    robberies.write(str_crimes)
                print(f"NUMBER OF PROCESSED ROBBERIES: {rob_sum}")
                print(f"DAY WITH MOST ROBBERIES: {day_most}")
                print(f"MONTH WITH MOST ROBBERIES: {month_most}")
                print(f"HOUR WITH MOST ROBBERIES: {hour_most}")
            except:
                print('An error has occurred while attempting to read and ' +
                        'process the given files')
    else:
        print('Invalid command-line arguments provided. ' +
                'Usage: crimetime.py crimes.tsv times.tsv robberies.tsv')


if __name__ == '__main__':
    main()
