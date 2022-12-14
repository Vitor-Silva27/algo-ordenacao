def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista


def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda, topo_direita = 0, 0

    for i in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[i] = direita[topo_direita]
            topo_direita += 1

        elif topo_direita >= len(direita):
            lista[i] = esquerda[topo_esquerda]
            topo_esquerda += 1

        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[i] = esquerda[topo_esquerda]
            topo_esquerda += 1

        else:
            lista[i] = direita[topo_direita]
            topo_direita += 1