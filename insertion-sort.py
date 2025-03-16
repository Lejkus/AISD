def insertion_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return 

    # iterujemy od drugiego elementu do końca
    for i in range(1, n):
        klucz = arr[i]  # wybieramy element, który chcemy wstawić
        j = i - 1  # patrzymy na poprzedni element
        
        print(f"\n Rozważamy liczbę {klucz} na pozycji {i}")

        # przesuwamy elementy w prawo, jeśli są większe od klucza
        while j >= 0 and arr[j] > klucz:
            print(f"Przesuwamy {arr[j]} z pozycji {j} na pozycję {j + 1}")
            arr[j + 1] = arr[j]
            j -= 1

        # wstawiamy klucz na właściwe miejsce
        arr[j + 1] = klucz
        print(" Wstawiamy klucz na pozycję:", j + 1)
        print(" Tablica po tej iteracji:", arr)


# testujemy na prostym przykładzie
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("\n Posortowana tablica:", arr)
