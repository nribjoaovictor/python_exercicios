def merge(lista, esquerda, meio, direita, compare, indice):
    metade_esquerda= lista[esquerda:meio]
    metade_direita= lista[meio:direita]
    i = j = 0
    k=esquerda
    while i < len(metade_esquerda) and j < len(metade_direita):
        if compare(metade_esquerda[i], metade_direita[j], indice):
            lista[k] = metade_esquerda[i]
            i += 1
        else:
            lista[k] = metade_direita[j]
            j+= 1
        k+= 1
    while i < len(metade_esquerda):
        lista[k] = metade_esquerda[i]
        i+= 1
        k+= 1
    while j < len(metade_direita):
        lista[k]=metade_direita[j]
        j+= 1
        k+= 1