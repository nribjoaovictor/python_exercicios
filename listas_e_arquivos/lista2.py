# 7. Agenda Telefônica
# Implemente uma agenda telefônica que armazene os contatos em um dicionário, onde a chave é o
# número de telefone e o valor é o nome do contato. Escreva funções para adicionar, remover e
# buscar contatos. Crie também uma função para exibir todos os contatos em ordem alfabética
def agendatelefonica(arquivo1): #07 falta terminar
    arquivo=open(arquivo1,"rt")
    linhas=arquivo.readline()
    dicionario={}
    lista=[]
    while linhas!="":
        linha=linhas.strip().split(", ")
        lista.append(linha)
        linhas=arquivo.readline()
    print(lista)
    for i in range(len(lista)):
        numero=lista[i][0]
        nome=lista[i][1]
        dicionario[numero]=nome
    arquivo.close()
    return dicionario
# def main():
#     nome_arquivo="bdagendatelefonica.txt"
#     print(agendatelefonica(nome_arquivo))
# main()

#-------------------------------------------------------------------------------------------------------------------------------------------

def tradutor(arquivo1,palavra): #02
    arquivo=open(arquivo1,"rt")
    linha=arquivo.readline()
    lista=[]
    dicionario={}
    while linha!="":
        linhas=linha.strip().split(",")
        lista.append(linhas)
        linha=arquivo.readline()
    for i in range(len(lista)):
        chave=lista[i][0]
        valor=lista[i][1]
        dicionario[chave]=valor
    arquivo.close()
    if palavra in dicionario:
        return dicionario[palavra]
    else:
        return ("A tradução não está disponível.")
# def main():
#     arq="dicionario.txt"
#     pal=input("palavra: ")
#     print(tradutor(arq,pal))
# main()


#-------------------------------------------------------------------------------------------------------------------------------------------

#verificar se consigo excluir diretamente do arquivo
def produto(arquivo1):
    arquivo=open(arquivo1,"rt")
    lista=[]
    dicionario={}
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lista.append(linhas)
        linha=arquivo.readline()
    for i in range(len(lista)):
        chave=[]
        valor=lista[i][0]
        chave.append(lista[i][1])
        chave.append(lista[i][2])
        dicionario[valor]=chave
    arquivo.close()
    return dicionario

#se eu colocasse o "a" ele irá realizar um append e com "w" irá adicionar, mas limpará o programa junto
def adicionar_produto(arquivo1,produto,valor,preco): #adicionando diretamente no arquivo
    arquivo=open(arquivo1,"+a")
    arquivo.write('\n')
    arquivo.write(produto+", ")
    arquivo.write(valor+", ")
    arquivo.write(preco)
    arquivo.close()

def remove_produto(dicionario,produto): #removendo utilizando a função de ler o arquivo
    for i in dicionario:
        if produto in dicionario:
            del(dicionario[produto])
        return dicionario
# def main():
#     arq="produtos.txt"
#     valor=int(input("1- adiciona, 2- remove, 3- apresenta os produtos"))
#     if valor==3:
#         arq="produtos.txt"
#         print(produto(arq))
#     elif valor==1:
#         arq="produtos.txt"
#         prod=input()
#         valor=input()
#         preco=input()
#         prodd=adicionar_produto(arq,prod,valor,preco)
#     else:
#         dicionario=produto(arq)
#         id=input()
#         print(remove_produto(dicionario,id))
# main()


#-------------------------------------------------------------------------------------------------------------------------------------------


#4. Megasena
# Construa um programa Python que use dicionario(s) para pesquisar a frequencia de ocorrência
# das dezenas da megasena. Pesquise e faça o download da base de dados dos resultados de
# sorteio da megasena. Transforme essa base de dados em um arquivo texto onde cada sorteio
# ocupa uma linha do arquivo. Crie uma função para fazer a contagem e uma função main para
# invocar esta função. Ao final, o programa deve exibir 2 colunas na tela: a dezena e sua respectiva
# contagem.

def mega_sena(arquivo1): #04
    arquivo=open(arquivo1,"rt")
    dicionario={}
    lista=[]
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split()
        lista.append(linhas)
        linha=arquivo.readline()
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j] in  dicionario:
                dicionario[lista[i][j]]+=1
            else:
                dicionario[lista[i][j]]=1
    arquivo.close()
    return dicionario
# def main():
#     arquivo_megasena="megasena.txt"
#     print(mega_sena(arquivo_megasena))
# main()
    
#------------------------------------------------------------------------------------------------------------------------------------------





    
    
    
