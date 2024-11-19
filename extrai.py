#progrma que conta palavras da biblia formato txt
def f_extrair(dicionario):
    dici={}
    for i in dicionario.keys():
        if dicionario[i][0]>1.75 and dicionario[i][1]>60:
            dici[i]=( dicionario[i][0],dicionario[i][1])
    return dici

def main():
    dic={'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro': (1.72, 66)}
    extrai=f_extrair(dic)
    print(extrai)
main()
    
