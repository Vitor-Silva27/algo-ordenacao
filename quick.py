def quicksort(lista, inicio, fim):
    if inicio < fim:
        p = particionamento(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)
    

def particionamento(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[fim], lista[i] = lista[i], lista[fim]
    return i
