def merge_sort(arr):
    # Caso base: Se o arranjo tem 1 ou menos elementos, já está ordenado
    if len(arr) <= 1:
        return arr

    # Divide o arranjo em duas metades
    meio = len(arr) // 2
    metade_esquerda = arr[:meio]
    metade_direita = arr[meio:]

    # Ordena cada metade de forma recursiva
    esquerda_ordenada = merge_sort(metade_esquerda)
    direita_ordenada = merge_sort(metade_direita)

    # Combina as duas metades ordenadas
    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    arr_ordenado = []
    i = j = 0

    # Compara os elementos de ambas as metades e os combina em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            arr_ordenado.append(esquerda[i])
            i += 1
        else:
            arr_ordenado.append(direita[j])
            j += 1

    # Se sobrarem elementos em alguma das metades, adiciona ao arranjo final
    arr_ordenado.extend(esquerda[i:])
    arr_ordenado.extend(direita[j:])
    
    return arr_ordenado

