def merge(esquerda, direita, compara, indice):
    arr_ordenado = []
    i = j = 0

    # Compara os elementos de ambas as metades usando a função 'compara' com o parâmetro 'indice'
    while i < len(esquerda) and j < len(direita):
        if compara(esquerda[i], direita[j], indice):
            arr_ordenado.append(esquerda[i])
            i += 1
        else:
            arr_ordenado.append(direita[j])
            j += 1

    # Se sobrarem elementos em alguma das metades, adiciona ao arranjo final
    arr_ordenado.extend(esquerda[i:])
    arr_ordenado.extend(direita[j:])

    return arr_ordenado