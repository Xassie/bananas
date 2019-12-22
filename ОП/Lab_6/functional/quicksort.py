def quicks(arr):
    """This module executes quick sort of the list.
        That's pretty much detailed."""
    if arr:
        return quicks([x for x in arr if x < arr[0]]) + \
               [x for x in arr if x == arr[0]] + \
               quicks([x for x in arr if x > arr[0]])

    return []


def checkitem(item):
    try:
        item = [float(i) for i in item]
        return item
    except ValueError:
        print('Error: your list has to contain only floats')