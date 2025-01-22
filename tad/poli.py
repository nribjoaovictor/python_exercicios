def new_poli(polinomio):
    lista=[]
    termo=""
    for i in range(len(polinomio)):
        if polinomio[i] not in ["+","-"]:
            termo+=polinomio[i]
        else:     
            lista.append(termo)
            termo=""
            if polinomio[i]=="-":
                termo="-"+termo
    if termo!="":
        lista.append(termo)
    return lista

def dicionario_poli(polinomio):
    lst_poli=new_poli(polinomio)
    dic={}
    for i in lst_poli:
        lst=i.split("x")
        if len(lst)==1:
            dic[0]=int(lst[0])
        elif len(lst)==2 and lst[0]!="" and lst[1]=="":
            dic[1]=int(lst[0])
        elif len(lst)==2 and lst[1]!="" and (lst[0] in ["","-"]):
            dic[int(lst[1])]=1
            if lst[0]=="-":
                dic[int(lst[1])]=-1
        else:
            dic[int(lst[0])]=int(lst[1])
    return dic

def main():
    polinomio="5x4-2x3+7x-45"
    print(dicionario_poli(polinomio))
main()