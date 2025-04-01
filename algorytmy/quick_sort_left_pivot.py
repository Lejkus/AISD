def quicksort_left(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]  # Pivot jako pierwszy element
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_left(left) + equal + quicksort_left(right)
