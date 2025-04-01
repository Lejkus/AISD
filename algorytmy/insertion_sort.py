def insertion_sort(arr):
    n = len(arr)   
    if n <= 1:
        return 
    for i in range(1, n):
        klucz = arr[i] 
        j = i - 1 
        while j >= 0 and arr[j] > klucz:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = klucz
    return arr