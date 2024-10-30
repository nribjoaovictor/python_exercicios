#criar uma lista com os vizinhos de um elemento matriz[i][j]
import random
def geramatriz(linhas,colunas,min,max):
    linhas_matriz=[]
    for i in range(linhas):
        colunas_matriz=[]
        for j in range(colunas):
            colunas_matriz.append(random.randint(min,max))
        linhas_matriz.append(colunas_matriz)
    return linhas_matriz

def f_print(matriz):
    quantidade_linhas=len(matriz)
    quantidade_colunas=len(matriz[0])
    for x in range(quantidade_linhas):
        for y in range(quantidade_colunas):
            print("%4d" %matriz[x][y], end="")
        print()

def f_vizinhos(matriz,posição_linha,posição_coluna):
    vizinhos=[]
    qnt_linhas=len(matriz)
    qnt_colunas=len(matriz[0])
    for linhas in range(posição_linha-1,posição_linha+2):
        for colunas in range(posição_coluna-1,posição_coluna+2):
            vizinhos.append(matriz[linhas][colunas])
    vizinhos.remove(matriz[posição_linha][posição_coluna])
    return vizinhos
            


