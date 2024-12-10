import random
def print_matriz(matriz_print):
    linhas=len(matriz_print)
    colunas=len(matriz_print[0])
    for i in range(linhas):
        for j in range(colunas):
            print("%4d" %matriz_print[i][j],end="")
        print()
def move_matriz(matriz):
    linhas_principal=len(matriz)
    colunas_principal=len(matriz[0])
    l=1
    for i in range(1,linhas_principal): 
        c=0
        for j in range(0,colunas_principal):
            matriz[i][j]=matriz[l][c]
            c+=1
        l+=1
    return matriz

def geramatriz(linha,coluna,minimo,maximo):
    li_matriz=[]
    valores=int()
    for i in range(linha):
        col_matriz=[]
        for j in range(coluna):
            col_matriz.append(random.randint(minimo,maximo))
        li_matriz.append(col_matriz)
    return li_matriz
def main():
    qnt_linhas=int(input())
    qnt_colunas=int(input())
    min=int(input())
    max=int(input())
    matriz=geramatriz(qnt_linhas,qnt_colunas,min,max)
    print_principal=print_matriz(matriz)
    movida=move_matriz(matriz)
    print("----------------------------------------------------------------------------------")
    print_movida=print_matriz(movida)
main()