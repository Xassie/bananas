import argparse


def quick_sort(arr):
    if arr: return quick_sort([x for x in arr if x<arr[0]]) + \
                   [x for x in arr if x==arr[0]] + \
                   quick_sort([x for x in arr if x>arr[0]])
    return []


def main():
    parser = argparse.ArgumentParser(description='Enter the list')
    parser.add_argument('-n', action='store', dest='N', default=None,
                        type=int, help='List separated by spaces')
    R = vars(parser.parse_args())
    n = R['N']

    if not n:
        while True:
            try:
                n = input('').split()
                n = [int(i) for i in n]
                break

            except ValueError:
                print('Numbers!')


        print(quick_sort(n))

if __name__ == '__main__':
    main()