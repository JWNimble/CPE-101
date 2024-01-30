"""
CPE101
Spring 2021
Author: Jack Forrester
"""


def is_lower(char:str)->bool:
    """Determined whether or not a given character is lowercase
    Args:
        char (str): a character in the english alphabet
    Returns:
        bool: True if lowercase, False otherwise
    Examples:
        >>> is_lower('j')
        True
        >>> is_lower('I')
        False
        >>> is_lower('z')
        True
    """

    return 97 <= ord(char) <= 122


def char_rot_13(char:str)->str:
    """Returns the ROT-13 encoding of a given character
    Args:
        char (str): a character
    Returns:
        str: the character 13 places forward or backward along the alphabet
    Examples:
        >>> char_rot_13('n')
        'a'
        >>> char_rot_13('J')
        'W'
        >>> char_rot_13('!')
        '!'
    """

    if char.isalpha():
        if 'Z' < char < 'n' or char < 'N':
            return chr(ord(char) + 13)
        else:
            return chr(ord(char) - 13)
    else:
        return char


def str_rot_13(my_str:str)->str:
    """Returns the ROT-13 encoding of a given multi-character string
    Args:
        my_str (str): string
    Returns:
        str: ROT-13 encoding of the string
    Examlples:
        >>> str_rot_13('abcd')
        'nopq'
        >>> str_rot_13('Secret')
        'Frperg'
        >>> str_rot_13('BiLl CiPhEr Is StIlL aLiVe!!!')
        'OvYy PvCuRe Vf FgVyY nYvIr!!!'
    """

    str_len = len(my_str)
    i = 0
    accumulation = ''
    while i < str_len:
        s = char_rot_13(my_str[i])
        accumulation += s
        i += 1
    return accumulation


def str_translate(my_str:str, old:str, new:str)->str:
    """Returns a new string where each occurrence of the old substring is 
    replaced by the new substring
    Args:
        my_str (str): the original string
        old (str): the substring to be replaced
        new (str): the substring to inserted in place of the old substring
    Returns:
        str: a new string in which the old substring has been replace with the
             new one
    Examples:
        >>> str_translate('I like turtles, I love turtles', 'turtles', 'trains')
        'I like trains, I love trains'
        >>> str_translate('TigerTigerTiger', 'Tiger', 'Tora')
        'ToraToraTora'
        >>> str_translate('x is the answer to the meaning of life', 'x', '42')
        '42 is the answer to the meaning of life'
    """

    str_len = len(my_str)
    old_len = len(old)
    i = 0
    while i < str_len:
        if my_str[i:i + old_len] == old: 
            my_str = my_str[0:i] + new + my_str[i + old_len:]
        i += 1
    return my_str


def reverse_substr(my_str:str, start:int, end:int)->str:
    """Returns a new string with a substring that starts at position 'start' and
    ends at position 'end' reversed
    Args:
        my_str (str): the complete string
        start (int): the starting position og the reverse substring
        end (int): the end position of the reversed substring
    Returns:
        str: a string with the substring at the start and end positions reverse
    Examples:
        >>> reverse_substr('Cobra', 0, 4)
        'arboC'
        >>> reverse_substr('I hate my doom desserts, man', 10, 22)
        'I hate my stressed mood, man'
        >>> reverse_substr('The Cake Is A Lie', 7, 7)
        'The Cake Is A Lie'
    """

    str_len = len(my_str)
    i = 0
    position = end
    accumulation = ''
    while position > start:
        position = end - i
        s = my_str[position]
        accumulation += s
        i += 1
    if start != end:
        if end == str_len - 1:
            return my_str[0:start] + accumulation
        else:
            return my_str[0:start] + accumulation + my_str[end + 1:]
    else:
        return my_str


if __name__ == '__main__':
    import doctest
    doctest.testmod()
