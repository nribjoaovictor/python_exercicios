import insere as i
def main():
    qnt_linhas=int(input())
    qnt_colunas=int(input())
    min=int(input())
    max=int(input())
    matriz=i.geramatriz(qnt_linhas,qnt_colunas,min,max)
    matriz_print=i.print_matriz(matriz)
    qnt_linhas=int(input())
    qnt_colunas=int(input())
    min=int(input())
    max=int(input())
    nova_matriz=i.geramatriz(qnt_linhas,qnt_colunas,min,max)
    matriz_print=i.print_matriz(nova_matriz)
    entrada=int(input())
    saida=int(input())
    matriz_insere=i.insere(matriz,nova_matriz,2,2)
    matriz_print=i.print_matriz(matriz_insere)
main()

