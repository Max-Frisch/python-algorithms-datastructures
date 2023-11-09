def merge_sort(arr):
    # base case, check if the arr is already down to 1 elemnt
    if len(arr) > 1:
        # split the array into 2 sub arrays
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursively repeating the splitting
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge the arays, while sorting through comparing
        i = 0  # left arr index
        j = 0  # right arr index
        k = 0  # merged arr index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # as sublists can be of different length, add the
        # "remainders" to the target list
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr)
print(arr)
