# Binary search is a fast "divide and conquer" search
# algorithm with a time complexity of O(log n)
# It requires an ALREADY sorted array/list


def binary_search(arr, start, end, target):
    # determine the "rounded down" midpoint
    mid = (start + end) // 2
    # if the mid-point IS the value, return True for success
    if arr[mid] == target:
        return True
    if arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(arr) - 1
target = 8  # the example number to be searched

# returns True, if found, False otherwise
print(binary_search(arr, start, end, target))
