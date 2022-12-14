def selection_sort(lista):
    for i in range(len(lista)-1):
        indice_menor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]