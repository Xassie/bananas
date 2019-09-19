# Python 3.7.2

from math import degrees, cos

# Entering number of degrees
while True:
    try:
        a = int(input('Enter integer representing degrees: '))
        break

    except ValueError:
        print("You're wrong. Try again.\n")

# Printing the result
print(cos(degrees(a))**2)