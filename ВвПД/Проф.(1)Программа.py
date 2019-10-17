# Python 3.7.2
# Calculating cosine of a powered by 2

from math import degrees, cos
import argparse


def main():
    parser = argparse.ArgumentParser(description="Program calculates "
                                                 "cosine powered by 2")
    parser.add_argument('-n', action='store', dest='n', default=None,
                        type=float, help='Degrees as float')
    R = parser.parse_args()
    a = R.n

    # Entering number of degrees
    if not a:
        while True:
            try:
                a = float(input('Enter number representing degrees: '))
                break

            except ValueError:
                print("You're wrong. Try again.\n")

    # Printing the result
    print(cos(degrees(a))**2)

if __name__ == '__main__':
    main()