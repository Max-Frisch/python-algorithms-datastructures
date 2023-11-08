def selection_sort(arr):
    # outer loop to cycle through the list, starting with the
    # first item as the current minimum
    for i in range(0, len(arr)-1):
        cur_min_idx = i
        # inner loop, iterating through the rest of the list to find the smallest/smaller item than the current min
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        # swap the elements
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]


arr = [2, 6, 5, 1, 3, 4, 9, 7]
selection_sort(arr)
print(arr)
