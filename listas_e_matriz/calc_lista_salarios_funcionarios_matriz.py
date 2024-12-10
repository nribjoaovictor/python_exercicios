def main():
    vendas=float(input())
    lst=[299,399,499,599,699,799,899,999]
    lst_cont=[0,0,0,0,0,0,0,0,0]
    valor=200+((9*vendas)/100)
    while vendas!=0:
        x=0
        if valor>999:
            lst_cont[8]+=1
        elif valor<299:
            lst_cont[0]+=1
        else:
            while lst[x]<valor:
                result=lst[x+1]
                x+=1
            print(result)
        lst_cont[x]+=1
        print(valor)
        print(lst_cont) 
        vendas=float(input())
        valor=200+((9*vendas)/100)
main()