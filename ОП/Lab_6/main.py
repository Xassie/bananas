""" Xassie
    КИ19-16/2б
    Вариант 19
"""


import argparse
from functional.quicksort import *


def cmd():
        parser = argparse.ArgumentParser(description='Enter the list in quotes.')
        parser.add_argument('N', action='store', help='List separated by spaces.')
        R = parser.parse_args()
        return R.N.split()


def main():
    num = checkitem(cmd())
    if num:
        print(quicks(num))


if __name__ == '__main__':
    main()
