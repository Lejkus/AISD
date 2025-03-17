# https://www.youtube.com/watch?v=2DmK_H7IdTo&t=1s
def heapify(arr, n, i):
    # Ustalamy, że największy element to korzeń
    największy = i  
    lewy = 2 * i + 1   # Lewy potomek
    prawy = 2 * i + 2 # Prawy potomek

    # Sprawdzamy, czy lewy potomek jest większy od korzenia
    if lewy < n and arr[lewy] > arr[największy]:
        największy = lewy

    # Sprawdzamy, czy prawy potomek jest większy od obecnego "największego"
    if prawy < n and arr[prawy] > arr[największy]:
        największy = prawy

    # Jeśli największy nie jest korzeniem, zamieniamy miejscami
    if największy != i:
        print(f"Zamieniamy {arr[i]} (index {i}) z {arr[największy]} (index {największy})")
        arr[i], arr[największy] = arr[największy], arr[i]

        # Rekurencyjnie budujemy kopiec dla poddrzewa
        heapify(arr, n, największy)


def heap_sort(arr):
    n = len(arr)

    # Budujemy kopiec (przekształcamy tablicę w kopiec)
    print("\nBudowanie kopca...")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print("Stan kopca:", arr)

    # Wydobywamy elementy jeden po drugim z kopca
    print("\nSortowanie kopca...")
    for i in range(n - 1, 0, -1):
        print(f"\nPrzenosimy {arr[0]} (korzeń) na koniec tablicy na pozycję {i}")
        arr[i], arr[0] = arr[0], arr[i]  # Zamieniamy miejscami korzeń z ostatnim elementem
        print("Tablica po zamianie:", arr)

        # Wywołujemy heapify na zmniejszonym kopcu
        heapify(arr, i, 0)
        print("Kopiec po naprawie:", arr)


# Testujemy na prostym przykładzie
arr = [9, 8, 3, 7, 11, 5, 6, 4, 1]
heap_sort(arr)
print("\nPosortowana tablica:", arr)
