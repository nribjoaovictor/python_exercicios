def loadFileNames(arquivo1):
    lista_nomes=[]
    arquivo=open(arquivo1,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip()
        lista_nomes.append(linhas)
        linha=arquivo.readline()
    arquivo.close()
    return lista_nomes

def loadBDSuper(arquivo2):
    arquivo=open(arquivo2,"rt",encoding="utf-8")
    dic={}
    dic_cod={}
    lista=[]
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lista.append(linhas)
        linha=arquivo.readline() 
    for i in range(len(lista)):
        dic["nome"]=lista[i][1]
        dic["categ"]=lista[i][2]
        dic["unidade"]=lista[i][3]
        dic["preco"]=lista[i][4]
        dic_cod[lista[i][0]]=dict(dic)
    arquivo.close()
    return dic_cod

def fazNF(d,arquivo3):
    lista=[]
    arquivo=open(arquivo3,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lista.append(linhas)
        linha=arquivo.readline()
    print(lista)
    arquivo.close()
    arquivo_saida=open("nf"+arquivo3,"+a",encoding="utf-8")

    #criando a tela de saída - Parte 1
    arquivo_saida.write("-"*120)
    arquivo_saida.write("\n")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("SUPERMERCADO BOA COMPRA")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("\n")
    arquivo_saida.write(" "*35)
    arquivo_saida.write("Av.Central, 1234 - Centro, Vitória")
    arquivo_saida.write("\n")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("CNPJ: 12.345.678/0001-99")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("\n")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("Telefone: (11) 1234-5678")
    arquivo_saida.write(" "*40)
    arquivo_saida.write("\n")
    arquivo_saida.write("-"*120)
    arquivo_saida.write("\n")

    #criando tela de saída - parte 2
    arquivo_saida.write("DATA: 18/12/2024")
    arquivo_saida.write(" "*70)
    arquivo_saida.write("HORA: 15: 34")
    arquivo_saida.write("\n")
    arquivo_saida.write("NOTA FISCAL: 00123456789")
    arquivo_saida.write("\n")
    arquivo_saida.write("ATENDENTE: João Silva")
    arquivo_saida.write("\n")
    arquivo_saida.write("-"*120)
    arquivo_saida.write("\n")

    #criando tela de saída - parte 3
    arquivo_saida.write("{:<5} {:<45} {:<12} {:<12} {:<12} {:<12}\n".format("COD", "DESCRIÇÃO", "QTD", "UN", "PREÇO", "TOTAL"))
    arquivo_saida.write("-" * 120)
    arquivo_saida.write("\n")
    valor_total=0
    for i in range(len(lista)):
        codigo = d[lista[i][0]]
        total = float(lista[i][1]) * float(codigo["preco"])
        valor_total+=total
        arquivo_saida.write("{:<5} {:<45} {:<12} {:<12} {:<12} {:<12.2f}\n".format(
            lista[i][0],
            codigo["nome"],
            lista[i][1],
            codigo["unidade"],
            codigo["preco"],
            total
        ))
    arquivo_saida.write("-"*120)
    arquivo_saida.write("\n")
    arquivo_saida.write("{:<50} {:<26} {:<8.2f}\n".format('','TOTAL:',valor_total))
    arquivo_saida.write("{:<50} {:<26} {:<8.2f}\n".format('','PAGAMENTO:',valor_total))
    arquivo_saida.write("{:<50} {:<26} {:<8}\n".format('','TROCO:','0'))
    arquivo_saida.write("-" * 120)
    arquivo_saida.write("\n")
    arquivo_saida.write("{:<30}{:<30}\n".format('','OBRIGADO POR COMPRAR NO SUPERMERCADO BOA COMPRA!'))

    arquivo_saida.close()

def main():
    arq="bdfilenames.txt"
    arq2=loadBDSuper("bdsupermercado.txt")
    nome=loadFileNames(arq)
    for x in nome:
        nf=fazNF(arq2,x)
main()



