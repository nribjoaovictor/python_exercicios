#loadmatriz(nome_arquiivo)
#salvamatriz(mat,nome_arquivo)
import exercicio_matriz as em
def main():
    matriz=em.geramatriz(10,10,1,10)
    print(matriz)
    print()
    print(em.extraimat(matriz,2,2,2,2))
    print()
main()



