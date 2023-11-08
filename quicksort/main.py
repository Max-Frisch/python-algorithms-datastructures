

def quicksort(nums, low, high):
    if low < high:
        partition_pos = partition(nums, low, high)
        quicksort(nums, low, partition_pos - 1)
        quicksort(nums, partition_pos + 1, high)
    return nums


def partition(nums, low, high):
    i = low
    j = high - 1
    pivot = nums[high]

    while i < j:
        while i < high and nums[i] < pivot:
            i += 1
        while j > low and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    if nums[i] > pivot:
        nums[i], nums[high] = nums[high], nums[i]

    return i


my_list = [22, 11, 88, 66, 55, 77, 33, 44]

quicksort(my_list, 0, len(my_list) - 1)

print(my_list)
