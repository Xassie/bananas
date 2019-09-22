# Python 3.7.2

"""   Вариант 19 
    Написать программу, вычисляющую углы треугольника по длинам его 
    сторон. Если невозможно сформировать треугольник из данных сторон (или 
    для вырожденного треугольника), тогда результатом должны быть все нули. 
    Углы должны быть записаны в градусах и округляются до целого числа 
    (стандартное округление).
"""

from math import degrees, acos


# Function to calculate one angle
def calc(a,c,b): 
    return round(degrees(acos((a**2 + c**2 - b**2) / (2 * a * c))))


# Getting and checking the sides of triangle
while True:

    try:
        a = input('Please enter valuables a, b and c separated by space: \n').split(' ')
        a = [ float(x) for x in a ]
        assert (len(a) == 3)
        break

    except ValueError:
        print('\nPlease make sure that all entered "numbers" are actually numbers\n')

    except AssertionError:
        print('\nPlease make sure that your triangle actually has 3 sides and no more or less\n')


# Making sure triangle exists and the providing calculation
a,b,c = a
degs = [0, 0, 0]
if ((a+b > c) and (b+c > a) and (a+c > b)): 
    degs = [calc(a,c,b), calc(a,b,c), calc(b,c,a)]

# Initializing the output
for i in degs:
    print(i, '°')
