def chamando(filename):
    lst=[]
    dic={}
    arquivo=open(filename,"rt")
    linha=arquivo.readline()
    while linha!="":
        linhas=linha.strip().split(", ")
        lista_coord_es=[]
        lista_coord_di=[]
        lista_coord_es.append(int(linhas[2]))
        lista_coord_es.append(int(linhas[3]))
        lista_coord_di.append(int(linhas[4]))
        lista_coord_di.append(int(linhas[5]))
        dic["Nome"]=linhas[0]
        dic["Email"]=linhas[1]
        dic["es"]=(lista_coord_es)
        dic["di"]=(lista_coord_di)
        dic["Carros"]=int(0)
        lst.append(dic)
        linha=arquivo.readline()
    arquivo.close()
    return lst

def new_est(es,di,email,empresa):
    dic={"nome":empresa,"email":email,"es":es,"di":di}
    return dic

def get_empresa(tadest):
    return tadest["nome"]
def get_email(tadest):
    return tadest["email"]
def get_num_carros(tadest):
    return tadest["carros"]
def set_num_carros(tadest,qnt):
    tadest["carros"]+=1

def area(tadest):
    lado_es=tadest["es"]
    lado_di=tadest["di"]
    area=(lado_di[0]-lado_es[0])*(lado_di[1]-lado_es[1])
    return area

def perimetro(tadest):
    lado_es=tadest["es"]
    lado_di=tadest["di"]
    perimetro=(lado_di[0]-lado_es[0])+(lado_di[1]-lado_es[1])
    return perimetro


def pertence(tadest,tadponto):
    if (tadest["es"][1]<tadponto[1]<tadest["di"][1]) and (tadest["es"][0]<tadponto[1]<tadest["di"][0]):
        return True
    else:
        return False
    

