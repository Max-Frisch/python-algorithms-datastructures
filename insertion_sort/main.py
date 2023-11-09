def insertion_sort(arr):
    # iterate through the list, starting at the 2nd idx [1]
    for i in range(1, len(arr)):
        j = i
        # inner loop, comparing the curr. pos with the pos
        # to the left, swapping the smallest no. to the left
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


arr = [2, 6, 5, 1, 3, 4, 9, 7]
insertion_sort(arr)
print(arr)
