# https://www.youtube.com/watch?v=g-PGLbMth_g&t=1s
def selection_sort(arr, n):
    # Przechodzimy przez całą tablicę
    for i in range(n):
        # Zakładamy, że minimalny element jest na pozycji i
        min_index = i

        print(f"Szukamy minimum w podtablicy od indeksu {i} do końca")
        
        # Szukamy najmniejszego elementu w pozostałej części tablicy
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                print(f"Znaleziono mniejsze: {arr[j]} (index {j}) < {arr[min_index]} (index {min_index})")
                min_index = j
        
        # Zamieniamy miejscami aktualny element z najmniejszym znalezionym
        print(f"Zamieniamy {arr[i]} (index {i}) z {arr[min_index]} (index {min_index})")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Tablica po tej iteracji:", arr ,"\n")


# Testujemy na prostym przykładzie
arr = [9, 8, 3, 7, 11, 5, 6, 4, 1]
n = len(arr)
selection_sort(arr, n)
print("\n","Posortowana tablica:", arr)

