def binary_search(data, followers):
    first = 0
    last = len(data) - 1

    while first <= last:
        midpoint = (first + last)//2
        if data[midpoint] == followers:
            return midpoint
        elif data[midpoint] < followers:
            first = midpoint+1
        else:
            last = midpoint-1
    return None
