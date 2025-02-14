def particiona(lst, inicio, fim, compara, indice):
    pivo=lst[fim]
    i=inicio-1
    for j in range(inicio, fim):
        if compara(lst[j], pivo, indice):
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i+1],lst[fim]=lst[fim],lst[i+1]
    return i+1
