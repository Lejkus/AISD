import random

# https://www.youtube.com/watch?v=Hoixgm4-P4M
def quicksort(arr, pivot_type):
    # funkcja rekurencyjnego quicksorta
    if len(arr) < 2:
        print("koniec rekurencji: ",arr)
        return arr

    # wybór pivota w zależności od opcji
    if pivot_type == 'left':
        pivot = arr[0]  
    elif pivot_type == 'random':
        pivot = random.choice(arr) 

    # podział na mniejsze, równe i większe od pivota
    left = []
    equal = []
    right = []

    for x in arr:
        if x < pivot:
            print(f"{x} jest mniejsze niż pivot {pivot}, dodajemy do lewej części")
            left.append(x)
        elif x == pivot:
            print(f"{x} jest równe pivotowi {pivot}, dodajemy do części 'equal'")
            equal.append(x)
        else:
            print(f"{x} jest większe niż pivot {pivot}, dodajemy do prawej części")
            right.append(x)

    print(f"lewo: {left}, równe: {equal}, rawo: {right}\n")

    # rekurencyjne sortowanie i scalanie
    return quicksort(left, pivot_type) + equal + quicksort(right, pivot_type)


# Przykładowe dane do testu
data = [10, 7, 8, 9, 1, 5, 3, 2, 6]
print(data)

#print("Sortowanie z pivotem jako skrajnie lewym elementem:")

#sorted_left_pivot = quicksort(data, pivot_type='left')
#print("\nWynik:", sorted_left_pivot)


#print("\nSortowanie z pivotem jako losowym elementem:")
sorted_random_pivot = quicksort(data, pivot_type='random')
print("\nWynik:", sorted_random_pivot)