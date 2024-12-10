import random
def geramatriz(linhas,colunas,min,max):
    linhas_matriz=[]
    for i in range(linhas):
        colunas_matriz=[]
        for j in range(colunas):
            colunas_matriz.append(random.randint(min,max))
        linhas_matriz.append(colunas_matriz)
    return linhas_matriz

def rotaciona(matriz):
    qnt_linhas=len(matriz)
    qnt_colunas=len(matriz[0])
    for li in range(qnt_linhas):
        cont_coluna=1
        for co in range(0,qnt_colunas):
            if co<(qnt_colunas-1):
                matriz[li][co]=matriz[li][cont_coluna]
            if co==qnt_colunas-1:
                matriz[li][qnt_colunas-1]=0
            cont_coluna+=1
    return matriz

def print_matriz(matriz_print):
    linhas=len(matriz_print)
    colunas=len(matriz_print[0])
    for i in range(linhas):
        for j in range(colunas):
            print("%4d" %matriz_print[i][j],end="")
        print()

def main():
    quantidade_li=int(input())
    quantidade_co=int(input())
    min=int(input())
    max=int(input())
    matriz_geramatriz=geramatriz(quantidade_li,quantidade_co,min,max)
    print_geramatriz=print_matriz(matriz_geramatriz)
    matriz_rotaciona=rotaciona(matriz_geramatriz)
    print("__________________________________")
    print_rotaciona=print_matriz(matriz_rotaciona)
main()
        