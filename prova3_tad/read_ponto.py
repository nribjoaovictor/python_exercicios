def chamando_arquivo(filename):
    lst=[]
    arquivo=open(filename,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(",")
        lst.append(linhas)
        linha=arquivo.readline()
    arquivo.close()
    return lst
