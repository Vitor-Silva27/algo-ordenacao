def shellSort(array, tamanho_array):
    intervalo = tamanho_array // 2
    while intervalo > 0:
        for i in range(intervalo, tamanho_array):
            valor_atual = array[i]
            cont = i
            while cont >= intervalo and array[cont - intervalo] > valor_atual:
                array[cont] = array[cont - intervalo]
                cont -= intervalo

            array[cont] = valor_atual
        intervalo = intervalo // 2