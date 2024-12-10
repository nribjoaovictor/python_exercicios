import q1 as q
def main():
    quantidade_linhas=int(input())
    quantidade_colunas=int(input())
    min=int(input())
    max=int(input())
    matriz=q.gera_matriz(quantidade_linhas,quantidade_colunas,min,max)
    print_matriz=q.matriz_print(matriz)
    print("____________________________________")
    triangulo_superior=q.f_triangulo_superior(matriz)
    print_matriz=q.matriz_print(triangulo_superior)
main()