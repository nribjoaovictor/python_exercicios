import mergesort_r as r
import mergesort_nr as nr

def bdcepsruas_read(filename):
    lst=[]
    arquivo=open(filename,"rt",encoding="utf-8")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lst.append(linhas)
        linha=arquivo.readline()
    arquivo.close()
    return lst

def compara_nr(lista, compare,indice):
    if len(lista) <= 1:
        return lista
    passo = 1
    while passo < len(lista):
        for inicio in range(0, len(lista), passo * 2):
            esquerda = inicio
            meio = inicio + passo
            direita = min(inicio + passo * 2, len(lista))
            nr.merge(lista, esquerda, meio, direita, compare, indice)
        passo *= 2
    return lista


def crescente(a,b,indice):
    return a[indice] <= b[indice]
def descrecente(a,b,indice):
    return a[indice] >= b[indice]

def saida(lst,filename):
    arquivo_saida=open(filename,"+a",encoding="utf-8")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            arquivo_saida.write(lst[i][j])
        arquivo_saida.write("\n")
    arquivo_saida.write("-------------------------------------------------------")
    arquivo_saida.write("\n")
    arquivo_saida.close()

def main():
    arquivo="bdcepsruas.txt"
    lista=bdcepsruas_read(arquivo)
    merge=compara_nr(lista,descrecente,5)
    arquivo_saida=saida(merge,"bdmergesort-nr.txt")
    merge=compara_nr(lista,crescente,4)
    arquivo_saida=saida(merge,"bdmergesort-nr.txt")
    merge=compara_nr(lista,descrecente,2)
    arquivo_saida=saida(merge,"bdmergesort-nr.txt")
main()



    