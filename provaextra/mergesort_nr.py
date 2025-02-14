def merge(lista, esquerda, meio, direita, compare, indice):
    # Criação das metades esquerda e direita
    metade_esquerda = lista[esquerda:meio]
    metade_direita = lista[meio:direita]
    i = j = 0
    k = esquerda

    # Processo de fusão, usando a função de comparação passada como parâmetro
    while i < len(metade_esquerda) and j < len(metade_direita):
        if compare(metade_esquerda[i], metade_direita[j], indice):
            lista[k] = metade_esquerda[i]
            i += 1
        else:
            lista[k] = metade_direita[j]
            j += 1
        k += 1

    # Adiciona os elementos restantes da metade esquerda
    while i < len(metade_esquerda):
        lista[k] = metade_esquerda[i]
        i += 1
        k += 1

    # Adiciona os elementos restantes da metade direita
    while j < len(metade_direita):
        lista[k] = metade_direita[j]
        j += 1
        k += 1
