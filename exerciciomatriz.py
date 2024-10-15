import random
#criar função para fazer as linhas aparecerem uma em baixo da outra
#def print_linhas(matriz_gerada):
#    tamanho_linhas=len(matriz_gerada)
#   tamanho_colunas=len(matriz_gerada[0])
#   for i in range(tamanho_linhas):
#        for j in range(tamanho_colunas):
        
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
    print(matriz)
main()