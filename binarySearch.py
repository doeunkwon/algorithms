def binarySearch(a, x):
    (left, right) = (0, len(a) - 1)
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
