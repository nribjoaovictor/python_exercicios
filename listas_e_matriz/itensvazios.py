def remove_itens(d):
#     dicionario={}
#     for i in d.keys():
#         if d[i]!=None:
#             dicionario[i]=d[i]
#     return dicionario
    lst=[]
    for k in d.keys():
        if d[k]==None:
            lst.append(k)
    for k in lst:
        del d[k]
    return d


def f_filtrador(d,valor):
    lst=[]
    for k in d.keys():
        if d[k]<valor:
            lst.append(k)
    for k in lst:
        del d[k]
    return d

# def f_lista(lista,lista2):
#     dicionario={}
#     if len( lista)==len(lista2):
#         for i in range(len(lista)):
#             for j in range(len(lista2)):
#                 dicionario[lista[i]]=lista2[j]
#     return dicionario
def f_lista(la,lb,lc):
    lista=[]
    for i in range(len(la)):
        d={la[i]:{lb[i]:lc[i]}}
        lista.append(d)
    return lista

               


def main():
    lst1=['S001', 'S002', 'S003', 'S004']
    lst2=['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
    lst3=[85, 98, 89, 92]
    dic=f_lista(lst1,lst2,lst3)
    print(dic)
main()