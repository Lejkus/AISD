def shell_sort_sedgewick(arr):
    n = len(arr)

    sedgewick_gaps = []

    k = 0
    while True:
        gap = 4**k + 3 * 2**(k-1) + 1 if k > 0 else 1
        if gap > n:
            break
        sedgewick_gaps.append(gap)
        k += 1
    for gap in reversed(sedgewick_gaps):

        for i in range(gap, n):
            temp = arr[i] 
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp

    return arr
