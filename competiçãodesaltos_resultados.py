def f_average(x):
    soma=0
    for j in range(len(x)):
        soma+=x[j]
    return (soma/len(x))
def main():
    lst=[]
    name=input()
    while name!="":
        for i in range(5):
            jump=float(input())
            lst.append(jump)
        average=f_average(lst)
        print("Athlete:",name)
        print("heels:",lst)
        print(("heel´s average: %.1f m") %(average))
        name=input()
main()

