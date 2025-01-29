def load_document(texto):
    arquivo=open(texto,"rt",encoding='utf-8')
    lista=[]
    linha=arquivo.readline()
    if linha=="":
        pass
    else:
        lista_paragrafo=[]
        while linha!="":
            linhas=linha.strip().split(" ")
            lista_paragrafo.append(linhas)
            linha=arquivo.readline()
    arquivo.close()
    return  lista_paragrafo

def cont_palavras(texto):
    contador_palavras=0
    for i in range(len(texto)):
        for k in range(len(texto[i])):
            contador_palavras+=len(texto[i][k])
    return contador_palavras

def maior_palavra(texto):
    maior=0
    palavra=""
    for i in range(len(texto)):
        for k in range(len(texto[i])):
            if len(texto[i][k]) > maior:
                maior=len(texto[i][k])
                palavra=texto[i][k]
    return (maior ,palavra)

def menor_palavra(texto):
    menor=100
    palavra=""
    for i in range(len(texto)):
        for k in range(len(texto[i])):
            if len(texto[i][k]) < menor and (texto[i][k])!= "" :
                menor=len(texto[i][k])
                palavra=texto[i][k]
    return (menor ,palavra)

def frequencia(texto):
    dic={}
    for i in range(len(texto)):
        for k in range(len(texto[i])):
            if (texto[i][k]) in dic:
                dic[(texto[i][k])]+=1
            else:
                dic[(texto[i][k])]=1
    return dic


def main():
    arquivo=load_document("python\TAD\paragrafo_texto.txt")
    print(arquivo)
    print(cont_palavras(arquivo))
    print(maior_palavra(arquivo))
    print(menor_palavra(arquivo))
    print(frequencia(arquivo))
main()

    