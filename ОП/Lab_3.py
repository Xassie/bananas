from random import randint
import argparse


def main():
     parser = argparse.ArgumentParser(description='You are allowed to enter '
                                          'the amount of generated numbers')
     parser.add_argument('-n', action='store', dest='N', default=None,
                        type=int, help='The amount of elements in the list')
     R = vars(parser.parse_args())
     N = R['N']

     if not N:
          while True:
               try:
                    N = int(input('Please enter what length the list should be.\n'))
                    break

               except ValueError:
                    print('Make sure that you\'ve entered integer')

     source = []
     similarities = []

     for i in range(0, N):
          source.append(randint(0, 100))

     print(source)

     while (len(source) != 0):
          check = source.pop(0)
          if (check in source):
               similarities.append(check)
               while check in source:
                    source.remove(check)

     print(similarities)

if __name__ == '__main__':
     main()
