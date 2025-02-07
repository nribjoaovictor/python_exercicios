def chamando_veiculo(filename):
    lst=[]
    arquivo=open(filename,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(",")
        lst.append(linhas)
        linha=arquivo.readline()
    arquivo.close()
    return lst

def new_ponto(x,y):
    lista=[]
    lista.append(x)
    lista.append(y)
    return lista

def get_x(tad_ponto):
    for i in tad_ponto:
        return int(i[0])

def get_y(tad_ponto):
    for i in tad_ponto:
        return (i[1])
    



