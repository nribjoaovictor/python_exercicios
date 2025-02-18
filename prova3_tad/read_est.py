import tadest as te
def chamando_arquivo(filename):
    lst=[]
    arquivo=open(filename,"rt",encoding="utf-8")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lst.append(te.new_est((int(linhas[2]),int(linhas[3])),(int(linhas[4]),int(linhas[5])),str(linhas[0]), str(linhas[1])))
        linha=arquivo.readline()
    arquivo.close()
    return lst
