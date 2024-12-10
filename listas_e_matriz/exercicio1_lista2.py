def main():
    lst=input()
    lst_veiculo=[]
    lst_prop=[]
    sub_lst_veiculo=[]
    sub_lst_prop=[]
    novalista=[]
    while lst!="":
        lst_veiculo.append(lst) 
        sub_lst_veiculo.append(lst_veiculo)
        lst_veiculo=[]
        lst=input()
    lst_proprietario=input()
    while lst_proprietario!="":
        lst_prop.append(lst_proprietario)
        sub_lst_prop.append(lst_prop)
        lst_prop=[]
        lst_proprietario=input()
    for i in range(len(sub_lst_veiculo)):
        cpf_carro=sub_lst_veiculo[i][3]
        for j in range(len(sub_lst_prop)):
            cpf_prop=[j][0]
            if cpf_carro==cpf_prop:
                novalista.append(sub_lst_veiculo[j])
                novalista.append(sub_lst_prop[j])
        print(novalista)
    #para completar é necessario fazer a separação por virgula dentro de cada sublinha

main()