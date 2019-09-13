from math import factorial as fac


while True:
    try:
        N = input('Please enter N and K separated by space:\n').split(' ')
        assert len(N) == 2
        N = [int(x) for x in N]
        N, K = N
        break

    except AssertionError:
        print('Make sure to enter just two numbers. No more. No less.\n')

    except ValueError:
        print('Make sure you\'ve entered integers.\n')

matrix = []

for n in range(0, N):
    matrix.append([])
    for k in range(0, K):
        if (k > n):
            matrix[n].append(0)
        else:
            matrix[n].append(
                int(fac(n + 1) / (fac(k + 1) * fac(n - k)))
            )

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

for n in range(0, N + 1):
    s = ''
    for k in range(0, K + 1):
        s += str(matrix[n][k]) + ' '
    print(s)