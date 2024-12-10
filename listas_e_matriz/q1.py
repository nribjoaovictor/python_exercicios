import random
def matriz_print(matriz):
    qnt_linhas=len(matriz)
    qnt_colunas=len(matriz[0])
    for i in range(qnt_linhas):
        for j in range(qnt_colunas):
            print("%4d" %matriz[i][j],end="")
        print()

def gera_matriz(linhas,colunas,min,max):
    linhas_matriz=[]
    for i in range(linhas):
        colunas_matriz=[]
        for j in range(colunas):
            colunas_matriz.append(random.randint(min,max))
        linhas_matriz.append(colunas_matriz)
    return linhas_matriz

def f_triangulo_superior(matriz):
    qnt_linhas=len(matriz)
    qnt_colunas=len(matriz[0]) 
    c=1
    for x in range(qnt_linhas):
        for y in range(c,qnt_colunas):
            matriz[x][y]=0
        c+=1
    return matriz

