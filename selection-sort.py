# https://www.youtube.com/watch?v=g-PGLbMth_g&t=1s
def selection_sort(arr, n):
    for i in range(n):
        min_index = i

        print(f"szukamy minimum w podtablicy od indeksu {i} do końca")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                print(f"znaleziono mniejsze: {arr[j]} (index {j}) < {arr[min_index]} (index {min_index})")
                min_index = j
        
        print(f"zamieniamy {arr[i]} (index {i}) z {arr[min_index]} (index {min_index})")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print("tablica po tej iteracji:", arr ,"\n")


arr = [9, 8, 3, 7, 5, 2, 4, 1]
n = len(arr)
selection_sort(arr, n)


