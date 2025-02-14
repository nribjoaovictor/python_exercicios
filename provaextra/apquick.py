import quicksort_nr as nr
import quicksort_r as r

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

def compara_nr(lst, compara, indice):
    lista = []
    lista.append((0,len(lst)-1))
    topo=0
    while topo < len(lista):
        inicio,fim=lista[topo]
        topo+= 1
        if inicio < fim:
            elem_comparacao=nr.particiona(lst, inicio, fim, compara, indice)
            lista.append((inicio, elem_comparacao-1))  
            lista.append((elem_comparacao+1, fim))    
    return lst

def compara_r(lst,inicio,fim,compara,indice):
    if inicio < fim:
        elem_comparacao=r.particiona(lst, inicio, fim, compara, indice)
        compara_r(lst, inicio, elem_comparacao-1, compara, indice)
        compara_r(lst, elem_comparacao+1, fim, compara, indice)
    return lst

def crescente(a,b,indice):
    return a[indice] <= b[indice]
def descrecente(a,b,indice):
    return a[indice] >= b[indice]

def saida(lst,filename):
    arquivo_saida=open(filename,"+a",encoding="utf-8")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            arquivo_saida.write(lst[i][j])
            arquivo_saida.write(", ")
        arquivo_saida.write("\n")
    arquivo_saida.write("-------------------------------------------------------")
    arquivo_saida.write("\n")
    arquivo_saida.close()

def main():
    arquivo="bdcepsruas.txt"
    lista=bdcepsruas_read(arquivo)
    #------------------------------------------------
    merge=compara_nr(lista,descrecente,5)
    arquivo_saida=saida(merge,"bdquicksort-nr.txt")
    merge=compara_nr(lista,crescente,4)
    arquivo_saida=saida(merge,"bdquicksort-nr.txt")
    merge=compara_nr(lista,descrecente,2)
    arquivo_saida=saida(merge,"bdquicksort-nr.txt")
    #--------------------------------------------------
    merge=compara_r(lista,0, len(lista)-1,descrecente,5)
    arquivo_saida=saida(merge,"bdquicksort-r.txt")
    merge=compara_r(lista,0, len(lista)-1,descrecente,4)
    arquivo_saida=saida(merge,"bdquicksort-r.txt")
    merge=compara_r(lista,0, len(lista)-1,descrecente,2)
    arquivo_saida=saida(merge,"bdquicksort-r.txt")
main()
