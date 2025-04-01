import random

def quicksort_random(arr):
    if len(arr) < 2:
        return arr

    pivot = random.choice(arr)  # Pivot losowy
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_random(left) + equal + quicksort_random(right)
