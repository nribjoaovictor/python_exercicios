def f_soma(x):
    soma=0
    for i in range(len(x)):
        soma+=x[i]
    return soma
def f_mult(y):
    multiplicação=1
    for j in range(len(y)):
        multiplicação=multiplicação*y[j]
    return multiplicação


def main():
    vetor=[]
    for i in range(5):
        num=int(input())
        vetor.append(num)
    multi=f_mult(vetor)
    soma=f_soma(vetor)
    print(vetor,multi,soma)
main()