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

def compara(lista, compare):
    if len(lista) <= 1:
        return lista

    passo = 1
    while passo < len(lista):
        for inicio in range(0, len(lista), passo * 2):
            esquerda = inicio
            meio = inicio + passo
            direita = min(inicio + passo * 2, len(lista))
            nr.merge(lista, esquerda, meio, direita, compare)
        passo *= 2
    return lista

def crescente(a,b):
    return a[0] <= b[0]
def descrecente(a,b):
    return a[0] >= b[0]

def saida(lst,filename):
    arquivo_saida=open(filename,"+a",encoding="utf-8")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            arquivo_saida.write(lst[i][j])
        arquivo_saida.write("\n")
    arquivo_saida.write("-----------------------------------------")
    arquivo_saida.close()

def main():
    arquivo="bdcepsruas.txt"
    lista=bdcepsruas_read(arquivo)
    merge=compara(lista,crescente)
    arquivo_saida=saida(merge,"bdmergesort-nr.txt")
    merge=compara(lista,descrecente)
    arquivo_saida=saida(merge,"bdmergesort-nr.txt")
    
main()



    