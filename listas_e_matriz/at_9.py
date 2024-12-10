def f_quad(x):
    soma=0
    for i in range(len(x)):
        soma+=(x[i]**2)
    return soma
def main():
    a=[]
    for i in range(10):
        num=int(input())
        a.append(num)
    soma_quad=f_quad(a)
    print(soma_quad)
main()