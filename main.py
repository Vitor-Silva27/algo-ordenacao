from cria_array import gera_array
from insertion import insertion_sort
from selection import selection_sort
from bubble import bubble_sort
from merge import merge_sort
from quick import quicksort
from shellsort import shellSort
import time

array_de_teste = gera_array(25_000)

inicio = time.time()

bubble_sort(array_de_teste)

fim = time.time()

print(fim - inicio)
