
def main():
    lst=input()
    lst_veiculo=[]
    lst_prop=[]
    lst_lst=[]
    lst_lst_prop=[]
    x=3
    while lst!="":
        lst_veiculo.append(lst) 
        lst_lst.append(lst_veiculo)
        lst_veiculo=[]
        lst=input()
    lst_proprietario=input()
    while lst_proprietario!="":
        lst_prop.append(lst_proprietario)
        lst_lst_prop.append(lst_prop)
        lst_prop=[]
        lst_proprietario=input()
    print(lst_lst_prop)
    print(lst_lst)
    x=0
    for i in range(len(lst_lst)):
        lst_lst[x].split(",")

main()

    

