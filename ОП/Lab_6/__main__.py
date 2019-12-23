""" Xassie
    КИ19-16/2б
    Вариант 19
"""


import argparse
import pytest
from functional import qsort


def cmd():
        parser = argparse.ArgumentParser(description='Enter the list in quotes.')
        parser.add_argument('-N', dest='N', action='store', default='', help='List separated by spaces.')
        parser.add_argument('--t', dest='T', action='store', default=False, type=bool, help='Do you want to run?')
        R = parser.parse_args()
        return R.N.split(), R.T


def main():
    num, test = cmd()
    num = qsort.checkitem(num)
    if test:
        pytest.main(['-v', 'functional\\tests.py'])
    if num:
        print(qsort.quicks(num))


if __name__ == '__main__':
    main()
