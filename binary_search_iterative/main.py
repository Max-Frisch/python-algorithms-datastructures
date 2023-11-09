# Binary search is a fast "divide and conquer"
# search algorithm with a time complexity of O(log n)
# It requires an ALREADY sorted array/list

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            # returns the index of the searched target
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    # returns -1 if the target was not found
    return -1


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(list, 5))
