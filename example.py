import sys
import os

sys.path.append(os.path.abspath("algorytmy"))

from heap_sort import heap_sort
from insertion_sort import insertion_sort
from quick_sort_left_pivot import quicksort_left 
from quick_sort_random_pivot import quicksort_random 
from selection_sort import selection_sort
from shell_sort_sedgewick import shell_sort_sedgewick

def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python

    if algorithm == 1:
        return insertion_sort(data)
    elif algorithm == 2:
        return shell_sort_sedgewick(data)
    elif algorithm == 3:
        return selection_sort(data)
    elif algorithm == 4:
        return heap_sort(data)
    elif algorithm == 5:
        return quicksort_left(data)
    elif algorithm == 6:
        return quicksort_random(data)
    else:
        raise ValueError("Invalid algorithm number")        

def main():
    print(f"Received arguments: {sys.argv}")

    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()
