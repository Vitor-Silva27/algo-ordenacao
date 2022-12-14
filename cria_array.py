import random

def gera_array(tamanho_do_array):
    arr = random.sample(range(1, tamanho_do_array+1), tamanho_do_array)
    return arr