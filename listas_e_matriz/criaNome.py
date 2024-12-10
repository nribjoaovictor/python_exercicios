import random

def gera_nome_Pessoa(lstnome, lstsobrenomes, tam):
    quant_nomes = 1
    quant_snomes = tam - quant_nomes

    nome = lstnome[random.randint(0, len(lstnome)-1)]

    acertos = 0
    lstsnomes = []
    while acertos < quant_snomes:
        sn = lstsobrenomes[random.randint(0,len(lstsobrenomes) -1)]
        if sn not in lstsnomes:
            lstsnomes.append(sn)
            acertos += 1
    for sobrenome in lstsnomes:
        nome = nome + " " + sobrenome
    return nome





def loadLista(nome_arquivo):
    lst = []
    arq = open(f'{nome_arquivo}', "rt")
    

    conteudo = arq.readline()
    while conteudo != "":
        lst.append(conteudo.strip())
        conteudo = arq.readline()

    arq.close()
    
    return lst

def main():
    lista_nomes = loadLista('nome.txt')
    lista_sobrenome = loadLista("sobrenome.txt")
    
    for i in range(10):
        print(gera_nome_Pessoa(lista_nomes, lista_sobrenome, 4))
if __name__ == "__main__":
    main()