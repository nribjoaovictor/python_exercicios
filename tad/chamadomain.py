import Chamado as ch
def main():
    lista_ch=[]
    arquivo=open("tad\chamadolista.txt","rt")
    linha=arquivo.readline()
    while linha!="":
        lista=linha.strip().split(", ")
        print(lista)
        pessoa=ch.tadpessoa(lista[0],lista[2],lista[3],lista[1])
        lista_ch.append(pessoa)
        linha=arquivo.readline()
    arquivo.close()

    for pessoa in lista_ch:
        if ch.maior(pessoa):
            print(ch.imc(pessoa),ch.getNome(pessoa),ch.getIdade(pessoa),ch.getAltura(pessoa),ch.getPeso(pessoa))
main()

        

