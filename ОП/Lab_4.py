""" Python 3.7.4
Шпаков Станислав
Вариант 19
"""

import argparse
from random import randint as rand


def quicks(arr):
    """This module executes quick sort of the list.
        That's pretty much detailed."""
    if arr:
        return quicks([x for x in arr if x < arr[0]]) + \
               [x for x in arr if x == arr[0]] + \
               quicks([x for x in arr if x > arr[0]])

    return []


def test_quicks():
    assert quicks([65, 42, 7, 89, 32, 1, ]) == [1, 7, 32, 42, 65, 89, ]
    assert quicks([56, 78, 3, 46, 86, 54, 68, ]) == [3, 46, 54, 56, 68, 78, 86, ]
    assert quicks([1]) == [1]
    assert quicks([]) == []


def cmd():
        parser = argparse.ArgumentParser(description='Enter the list in quotes.')
        parser.add_argument('N', action='store', help='List separated by spaces.')
        R = parser.parse_args()
        return R.N.split()


def checkitem(item):
    try:
        item = [int(i) for i in item]
        return item
    except ValueError:
        print('Error: your list has to contain only integers')


def main():
    num = checkitem(cmd())
    if num:
        print(quicks(num))


if __name__ == '__main__':
    main()
