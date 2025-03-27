def shell_sort_sedgewick(arr):
    n = len(arr)

    sedgewick_gaps = []

    # k to numer kolejnego odstępu podstawiony do wzoru
    k = 0
    while True:
        gap = 4**k + 3 * 2**(k-1) + 1 if k > 0 else 1
        # gdy odstęp będzie wieksz od dlugosci tablicy przerywamy [1,8,23,77,281,...]
        if gap > n:
            break
        sedgewick_gaps.append(gap)
        k += 1

    print("sadgewick gaps: ",sedgewick_gaps)

     # iterujemy przez odstępy od największego do najmniejszego
    for gap in reversed(sedgewick_gaps):
        print("\n----- SORTUJEMY DLA ODSTĘPU:", gap, "-----\n")

        for i in range(gap, n):
            temp = arr[i]  # pobieramy wartość do wstawienia
            j = i

            print(f"Rozważamy liczbę {temp} na pozycji [{i}] <- index")

            # sortowanie przez wstawianie dla tej podtablicy
            while j >= gap and arr[j - gap] > temp:
                print(f"Zamieniamy {arr[j - gap]} (index {j-gap}) z {arr[j]} (index {j})")
                arr[j] = arr[j - gap]
                j -= gap
            
            # wstawiamy liczbę na właściwe miejsce
            arr[j] = temp

            print("Tablica po tej iteracji:", arr ,"\n")

    return arr

# Test
print(shell_sort_sedgewick([9, 8, 3, 7, 11, 5, 6, 4, 1, 12]))  # [1, 3, 4, 5, 6, 7, 8, 9]
