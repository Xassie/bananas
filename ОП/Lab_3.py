# Python 3.7.4

""" Шпаков Станислав
    Ки19-16/2б
    Вариант 19
"""

from random import randint   # to fill the source
import argparse   # to make cmd useful


def main():
    # cmd usage
    parser = argparse.ArgumentParser(description="You're allowed to enter the "
                                                 "amount of generated numbers")
    parser.add_argument('-n', action='store', dest='N', default=None,
                        type=int, help='The amount of elements in the list')
    R = vars(parser.parse_args())
    N = R['N']
    del parser, R

    # checking the input
    if not N:
        while True:
            try:
                N = int(input('Enter what length this list should be.\n'))
                break
            except ValueError:
                print('Make sure that you\'ve entered integer')

    source = []
    similarities = []

    # filling the list
    for i in range(0, N):
        source.append(randint(0, 100))

    print(source, '\n')

    # getting similar numbers
    while (len(source) != 0):
        check = source.pop(0)
    if (check in source):
        similarities.append(check)
        while check in source:
            source.remove(check)

    print(similarities)


if __name__ == '__main__':
    main()
