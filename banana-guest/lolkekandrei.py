from math import sqrt

print('something')
flag = True

while flag:

    try:
        n = int(input())
        k = int(input())
        flag = False
    
    except ValueError:
        print('Integer values please')

print((((k + sqrt(k*k + 4))/2) + (k - sqrt(k**2 + 4))/2) / sqrt(5))