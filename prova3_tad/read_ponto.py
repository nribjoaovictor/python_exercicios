import tadponto as tp
def chamando_arquivo(filename):
    lst=[]
    arquivo=open(filename,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(",")
        ponto = tp.new_ponto(int(linhas[0]), int(linhas[1]))
        lst.append(ponto)
        linha=arquivo.readline()
    arquivo.close()
    return lst
