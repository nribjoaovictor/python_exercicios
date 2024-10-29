import random 
#falta criar as condionais que impossibilitam de acontecer
#ver videos sobre arquivos python
def print_matriz(matriz_print):
    linhas=len(matriz_print)
    colunas=len(matriz_print[0])
    for i in range(linhas):
        for j in range(colunas):
            print("%4d" %matriz_print[i][j],end="")
        print()
def insere(matriz,nova_matriz,entrada,saida):
    linhas_matriz=len(matriz)
    colunas_matriz=len(matriz[0])
    linhas_insere=len(nova_matriz)
    colunas_insere=len(nova_matriz[0])
    l=0
    for x in range(entrada,entrada+linhas_insere):
        c=0
        for y in range(saida,saida+colunas_insere):
            matriz[x][y]=nova_matriz[l][c]
            c+=1
        l+=1
    return matriz     
def geramatriz(linha,coluna,minimo,maximo):
    li_matriz=[]
    for i in range(linha):
        col_matriz=[]
        for j in range(coluna):
            col_matriz.append(random.randint(minimo,maximo))
        li_matriz.append(col_matriz)
    return li_matriz
