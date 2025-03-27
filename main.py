#Anna Semrau 164294
#Jakub Walkowiak 165120
import random
from time import time
def get_time(time_start: float, time_end: float):
  return(round(float(format(time_end - time_start, "f")) * 1000, 5))
def insertion_sort(arr):
    # iterujemy od drugiego elementu
    for i in range(1, len(arr)):
        klucz = arr[i]  # wybieramy element, który chcemy wstawić
        j = i - 1  # patrzymy na poprzedni element
        # przesuwamy elementy w prawo, jeśli są większe od klucza
        while j >= 0 and arr[j] > klucz:
            arr[j + 1] = arr[j]
            j -= 1
        # wstawiamy klucz na właściwe miejsce
        arr[j + 1] = klucz
    return arr

def selection_sort(arr):
    # Przechodzimy przez całą tablicę
    for i in range(len(arr)):
        # Zakładamy, że minimalny element jest na pozycji i
        min_index = i
        # Szukamy najmniejszego elementu w pozostałej części tablicy
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Zamieniamy miejscami aktualny element z najmniejszym znalezionym
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def shell_sort_sedgewick(arr):
    sedgewick_gaps = []
    # k to numer kolejnego odstępu podstawiony do wzoru
    k = 0
    while True:
        gap = 4**k + 3 * 2**(k-1) + 1 if k > 0 else 1
        # gdy odstęp będzie wieksz od dlugosci tablicy przerywamy [1,8,23,77,281,...]
        if gap > len(arr):
            break
        sedgewick_gaps.append(gap)
        k += 1
     # iterujemy przez odstępy od największego do najmniejszego
    for gap in reversed(sedgewick_gaps):
        for i in range(gap, len(arr)):
            temp = arr[i]  # pobieramy wartość do wstawienia
            j = i
            # sortowanie przez wstawianie dla tej podtablicy
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # wstawiamy liczbę na właściwe miejsce
            arr[j] = temp
    return arr

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
        arr[i], arr[największy] = arr[największy], arr[i]
        # Rekurencyjnie budujemy kopiec dla poddrzewa
        heapify(arr, n, największy)

def heap_sort(arr):
    # Budujemy kopiec (przekształcamy tablicę w kopiec)
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    # Wydobywamy elementy jeden po drugim z kopca
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Zamieniamy miejscami korzeń z ostatnim elementem
        # Wywołujemy heapify na zmniejszonym kopcu
        heapify(arr, i, 0)
    return arr

def quick_left(arr):
  if len(arr)<=1:
      return arr
  pivot=arr[0]
  # Podział tablicy na trzy części
  lower = [x for x in arr if x < pivot]    # Elementy mniejsze od pivota
  equal = [x for x in arr if x == pivot]   # Elementy równe pivotowi
  greater = [x for x in arr if x > pivot]  # Elementy większe od pivota
  return quick_left(lower) + equal + quick_left(greater)

def quick_random(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[random.randint(0, len(arr) - 1)] 
  # Podział tablicy na trzy części
  lower = [x for x in arr if x < pivot]    # Elementy mniejsze od pivota
  equal = [x for x in arr if x == pivot]   # Elementy równe pivotowi
  greater = [x for x in arr if x > pivot]  # Elementy większe od pivota
  # Rekurencyjne sortowanie lewej i prawej części
  return quick_random(lower) + equal + quick_random(greater)

print("Wybierz jak ma być ułożony wygenerowany ciąg:")
print("\n1. losowo \n2. rosnąco \n3. malejąco \n4. stale \n5. A-kształtnie")
uklad=int(input("Podaj układ do wygenerowania: "))

ilosc=int(input("\nPodaj proszę długość tego ciągu: "))

ciag = []
for i in range(ilosc):
  match uklad:
    case 1:
      ciag.append(random.randint(-100, 100))
    case 2:
      ciag.append(i)
    case 3:
      ciag.append(-i)
    case 4:
      ciag.append(1)
    case 5:
      ciag.append(0)
if (uklad==5):
  rozmiar=ilosc//2 if ilosc%2==0 else ilosc//2+1
  for j in range(rozmiar):
    ciag[j]=j
    ciag[-j-1]=j
print("\n",ciag)

print("\nWybierz jakim algorytmem ma być sortowany ciąg:")
print("\n1. insertion \n2. selection \n3. quick random \n4. heap \n5. quick left \n6. shell")
algo=int(input("Podaj algorytm do wykorzystania: "))
match algo:
    case 1:
      start_time = time()
      print(insertion_sort(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")
    case 2:
      start_time = time()
      print(selection_sort(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")
    case 3:
      start_time = time()
      print(quick_random(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")
    case 4:
      start_time = time()
      print(heap_sort(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")
    case 5:
      start_time = time()
      print(quick_left(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")
    case 6:
      start_time = time()
      print(shell_sort_sedgewick(ciag))
      end_time = time()
      time_taken = get_time(start_time, end_time)
      print(f"Czas: {time_taken} ms")