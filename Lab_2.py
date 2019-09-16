from math import factorial as fac
import argparse


# cmd interface
parser = argparse.ArgumentParser(description='You can enter matrix\'s size N x'
                                             ' K beforehand via --n and --k')
parser.add_argument('--n', action='store', dest='N', default=None,
                    type=int, help='Amount of lines in the matrix')
parser.add_argument('--k', action='store', dest='K', default=None,
                    type=int, help='Amount of columns in the matrix')
R = vars(parser.parse_args())
N, K = [R['N'], R['K']]
del R, parser


# if valuables are not defined then input
if not (N and K):

    while True:
        try:
            N = input('Please enter integer numbers N and '
                      'K separated by space:\n').split(' ')
            N = [int(x) for x in N]
            assert len(N) == 2
            N, K = N
            break

        except AssertionError:
            print('Make sure to enter just two numbers. No more. No less.\n')

        except ValueError:
            print('Make sure you\'ve entered integers.\n')

matrix = []

# Actually filling in all the numbers
for n in range(0, N):
    matrix.append([])
    for k in range(0, K):
        if (k > n):
            matrix[n].append(0)
        else:
            matrix[n].append(
                int(fac(n + 1) / (fac(k + 1) * fac(n - k)))
            )

# Calculating averages
matrix.append([])
for k in range(0, K):
    calc = 0
    for n in range(0, N):
        calc += matrix[n][k]
    matrix[N].append(calc)

for n in range(0, N):
    calc = 0
    for k in range(0, K):
        calc += matrix[n][k]
    matrix[n].append(calc)

matrix[N].append(0)

# Output that is actually not necessary ¯\_(ツ)_/¯
blanks = N//5 + 2

for n in range(0, N + 1):
    s = ''
    for k in range(0, K + 1):
        s += str(matrix[n][k]).center(blanks, ' ')
    print(s)
