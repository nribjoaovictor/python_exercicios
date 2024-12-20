import math 
def remove_itens(d): #01
    lst=[]
    for k in d.keys():
        if d[k]==None:
            lst.append(k)
    for k in lst:
        del d[k]
    return d

def f_filtrador(d,valor): #02
    lst=[]
    for k in d.keys():
        if d[k]<valor:
            lst.append(k)
    for k in lst:
        del d[k]
    return d

def f_lista(la,lb,lc): #03
    lista=[]
    for i in range(len(la)):
        d={la[i]:{lb[i]:lc[i]}}
        lista.append(d)
    return lista

def agrupa_lista(lista): #05
    list=[]
    list1=[]
    list2=[]
    dic={"amarelo":list,"azul":list1,"vermelho":list2}
    for i in range(len(lista)):
        if lista[i][0]=='amarelo':
            list.append(lista[i][1])
            dic["amarelo"]=list
        elif lista[i][0]=="azul":
            list1.append(lista[i][1])
            dic["azul"]=list1
        elif lista[i][0]=="vermelho":
            list2.append(lista[i][1])
            dic["vermelho"]=list2
    return dic

def repartir(dicionario): #06
    lst=[]
    for i in dicionario:
        tamanho=len(dicionario[i])
        print(tamanho)
    for j in range(tamanho):
        dic={}
        for k in dicionario:
            dic[k]=dicionario[k][j]
            print(dic)
        lst.append(dic)
    return lst

def remove(dicionario,id): #07
    lista=[]
    for i in range(len(dicionario)):
        for j in dicionario[i]:
            if dicionario[i][j]==id:
                lista.append(i)
    for k in lista:
        del dicionario[k]
    return dicionario

def cep_casas(nome_arq): #08
    arq=open(nome_arq,"rt")
    d={}
    lista=[]
    linhas=arq.readline()
    while linhas!="":
        linha=linhas.strip().split(", ")
        print(linha)
        lista.append(linha)
        linhas=arq.readline()
    for i in range(len(lista)):
        cep=lista[i][0]
        casa=int(lista[i][1])
        if cep not in d:
            d[cep]=[casa]
        elif cep in d:
            d[cep].append(casa)
    arq.close()
    return d
# def main():
#     nome_arquivo="cep.txt"
#     print(cep_casas(nome_arquivo))
# main()

def f_extrair_dicionario(lista,chave): #09
    lst=[]
    for i in lista:
        for j in i:
            if chave==j:
                lst.append(i[j])
    return lst
# def main():
#     lista=[{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92,
# 'Ciência': 88}]
#     chave="Ciência"
#     print(f_extrair_dicionario(lista,chave))
# main()

def dicionario_for_lista(dicionario): #11
    lista=[]
    for i in dicionario:
        lst=[]
        lst.append(i)
        lst.append(dicionario[i])
        lista.append(lst)
    return lista
# def main():
#     dicionario={1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
#     print(dicionario_for_lista(dicionario))
# main()

def f_filtar_numeros_pares(dicionario): #12
    dic={}
    for i in dicionario:
        lst=[]
        for j in dicionario[i]:
            if (j%2)==0:
                lst.append(j)
        dic[i]=lst
    return dic
# def main():
#     dicionario={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#     print(f_filtar_numeros_pares(dicionario))
# main()

#fazer chamar ele mesmo e mais o resto da lista, depois anda um elemento no dicionario
# [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]},
# {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
def f_cartesiano(dicionario): #13
    tamanho=len(dicionario)
    dicionario_final=[]
    for i in dicionario:
        print(i)
        for k in dicionario:
            print(k)
            dic={}
            dic[i]=dicionario[i]
            if i == k :
                continue
            elif i != k:
                dic[k]=dicionario[k]
                print(dic)
            dicionario_final.append(dic)
    return dicionario_final
# def main():
#     dicionario={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#     print(f_cartesiano(dicionario))
# main()

def f_maiores_valores(dicionario,n): #14
    lst_maior=[]
    maior=0
    chave=""
    contador=0
    while contador<n:
        for i in dicionario:
            if maior>=dicionario[i]:
                continue
            else:
                maior=dicionario[i]
                chave=i
        lst_maior.append(chave)
        del dicionario[chave]
        contador+=1
        maior=0
    return lst_maior
# def main():
#     dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
#     n=int(input("quantidade de valores"))
#     print(f_maiores_valores(dic,n))
# main()

#{'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
#saída: ['VI', 'VIII', 'X']
def f_menores_chaves(dicionario): #15
    tamanho_dicionario=len(dicionario)
    maior=math.inf
    print(maior)
    lista_menores=[]
    chave=''
    contador=0
    while contador<tamanho_dicionario:
        for i in dicionario:
            for j in dicionario[i]:
                tamanho=len(dicionario[i])
                if tamanho<maior:
                    chave=i
                    maior=tamanho
                else:
                    continue
        lista_menores.append(chave)
        del dicionario[chave]
        maior=math.inf
        contador+=1
    return lista_menores
# def main():
#     dicionario={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
#     print(f_menores_chaves(dicionario))
# main()

# Dicionário de entrada:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Dicionário de saída:
# {10: 2, 40: 2, 20: 2, 70: 1, 80: 1}
def f_frequencia(dicionario):
   pass 




                
                


    

