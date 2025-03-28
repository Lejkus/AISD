# https://www.youtube.com/watch?v=2DmK_H7IdTo&t=1s

def heapify(arr, n, i):
    # ustalamy, że największy element to korzeń
    największy = i  
    lewy = 2 * i + 1   # lewy potomek
    prawy = 2 * i + 2 # prawy potomek

    # arr = [3, 9, 2, 1, 4, 5]
    # korzeń (i = 0) = 3
    # lewy potomek (1) = 9
    # prawy potomek (2) = 2

    # największy element to 9, więc zamieniamy 3 z 9.
    # arr = [9, 3, 2, 1, 4, 5]


    # sprawdzamy, czy lewy potomek jest większy od korzenia
    if lewy < n and arr[lewy] > arr[największy]:
        największy = lewy

    # sprawdzamy, czy prawy potomek jest większy od obecnego "największego"
    if prawy < n and arr[prawy] > arr[największy]:
        największy = prawy

    # jeśli największy nie jest korzeniem, zamieniamy miejscami
    if największy != i:
        print(f"zamieniamy {arr[i]} (index {i}) z {arr[największy]} (index {największy})")
        arr[i], arr[największy] = arr[największy], arr[i]

        # rekurencyjnie budujemy kopiec dla poddrzewa
        heapify(arr, n, największy)


def heap_sort(arr):
    n = len(arr)

    # budujemy kopiec (przekształcamy tablicę w kopiec)
    print("\nbudowanie kopca...")
    # od połowy zaokrąglonej w dół, do 0 , co krok -1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print("stan kopca:", arr)

    # wydobywamy elementy jeden po drugim z kopca
    print("\nsortowanie kopca...")
    for i in range(n - 1, 0, -1):
        print(f"\nprzenosimy {arr[0]} (korzeń) na koniec tablicy na pozycję {i}")
        arr[i], arr[0] = arr[0], arr[i]  # zamieniamy miejscami korzeń z ostatnim elementem
        print("tablica po zamianie:", arr)

        # wywołujemy heapify na zmniejszonym kopcu
        heapify(arr, i, 0)
        print("kopiec po naprawie:", arr)


# Testujemy na prostym przykładzie
arr = [9, 8, 3, 7, 11, 5, 6, 4, 1]
heap_sort(arr)
print("\nposortowana tablica:", arr)
