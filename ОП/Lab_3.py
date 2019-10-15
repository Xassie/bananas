# Python 3.7.4

""" Шпаков Станислав
    Ки19-16/2б
    Вариант 19
"""

from random import randint   # to fill the source
import argparse   # to make cmd useful


def positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive"
                                         "int value" % value)
    return ivalue


def main():
    # cmd usage
    parser = argparse.ArgumentParser(description="You're allowed to enter the "
                                                 "amount of generated numbers")
    parser.add_argument('-n', action='store', dest='n', default=None,
                        type=positive, help='Amount of elements in the list')
    parser.add_argument('-r', action='store', dest='r', default=50,
                        type=positive, help='What\'s the max random number')

    R = parser.parse_args()
    N, r = R.n, R.r

    # checking the input
    if not N:
        while True:
            try:
                N = int(input('Enter what length this list should be.\n'))
                if N <= 0:
                    print('')
                    continue
                break
            except ValueError:
                print('Make sure that you\'ve entered pos integer')
            

    source = tuple([randint(0, r) for i in range(0, N)])
    unique = []
    similarities = []

    for i in source:
        if i not in unique:
            unique.append(i)
        elif i not in similarities:
            similarities.append(i)

    print(source, '\n', similarities)


if __name__ == '__main__':
    main()
