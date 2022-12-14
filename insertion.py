def insertion_sort(lista):
    for i in range(1, len(lista)):
        elemento_atual = lista[i]
        n = i-1
        while n >= 0 and lista[n] > elemento_atual:
            lista[n+1] = lista[n]
            n = n-1
        lista[n+1] = elemento_atual