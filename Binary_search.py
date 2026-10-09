def binary_search(num_list, x):

    """
    Binary Search algorithm  is dividing a list of values in half and start the
    search of a specfic number between left and right using midpoint.

    Args:
        Num_list contains a list of numbers and the program will search through
        the list from the chosen number.

    Returns:
        A sorted list of integers.

    """

    lower = 0
    higher = len(num_list) - 1

    while lower <= higher:
        midpoint = lower + (higher - lower) // 2

        if num_list[midpoint] < x:
            lower = midpoint + 1
        elif num_list [midpoint] > x:
            higher = midpoint - 1
        else:
            return midpoint

    return -1

num_list = [2, 3, 4, 10, 40]
x = 10
result = binary_search(num_list, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in list.")
