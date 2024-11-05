#dicionario={} #elementos do dicionario = entradas, cada entrada é formada por 2 (par de valores) valores, a chave e o valor
# #chave e valor => d={"SP":"São Paulo", "MG": "Minas Gerais"} primeiro par SP e São Paulo
# chave SP e valor São Paulo
# a primeira parte do par é a chave para ter a outra parte
# d=["MG"] => retorno = "Minas Gerais"
#como incluir nova entrada:
#d=["RJ"]="Rio de Janeiro"
#alteração é da msm forma para incluir
#d=["MG"]= "Minas", como já tem MG,irá alterar
#excluir => del
#del d["SP"]
#irá excluir São Paulo
#dicionario não tem ordem
#list(d.keys()) => retornará uma lista com os elementos chaves
#list(d.value())=> retornará uma lista com os valores
#list(d.itens())=> retornará uma tupla com os valores e as chaves
#d.keys() => riá retornar o dicionário apenas com as chaves
#for k in chaves:
#   print("chaves":,k,"valor:", d[k])
#import os => apagar a tela do prompt de comandos
#   os.system("cls")
#d={"sp",:{"nome":"são paulo","pop":546848, "pib":545786}}
#print(d["sp"][pib])
#545786
def main():
    d={"SP":"São Paulo","MG":"Minas Gerais","AJU":"Aracaju"}
    D={}
    x=0
    for i in d.keys():
        D[i]=d[i]
    print(d)
    print(D)
main()
#rodar no python tutor para entender os dicionarios
