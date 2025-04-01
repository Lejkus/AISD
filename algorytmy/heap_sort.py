def heapify(arr, n, i):

    największy = i  
    lewy = 2 * i + 1 
    prawy = 2 * i + 2

    if lewy < n and arr[lewy] > arr[największy]:
        największy = lewy
    if prawy < n and arr[prawy] > arr[największy]:
        największy = prawy
    if największy != i:
        arr[i], arr[największy] = arr[największy], arr[i]

        heapify(arr, n, największy)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  

        heapify(arr, i, 0)
    return arr
