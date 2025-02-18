import tadponto as tp
def new_est(es,di,email,empresa):
    dic={"nome":empresa,"email":email,"es": tp.new_ponto(es[0],es[1]),"di":tp.new_ponto(di[0],di[1]),"carros":0}
    return dic

def get_empresa(tadest):
    return tadest["nome"]
def get_email(tadest):
    return tadest["email"]
def get_num_carros(tadest):
    return tadest["carros"]
def set_num_carros(tadest,qnt):
    tadest["carros"]=qnt

def area(tadest):
    lado1 = tp.distancia(tadest["es"], tadest["di"])
    ds = tp.new_ponto(tp.get_x(tadest["es"]), tp.get_y(tadest["di"]))
    ei = tp.new_ponto(tp.get_x(tadest["di"]), tp.get_y(tadest["es"]))
    lado2 = tp.distancia(ds, ei)
    area = lado1*lado2
    return area

def perimetro(tadest):
    lado1 = tp.distancia(tadest["es"], tadest["di"])
    ds = (tadest["es"][0], tadest["di"][1])
    ei = (tadest["es"][1], tadest["di"][0])
    lado2 = tp.distancia(ds, ei)
    perimetro=(lado1+lado2)*2
    return perimetro

def pertence(tadest,tadponto):
    esquerda_X = int(tadest["es"][0])
    esquerda_y = int(tadest["es"][1])
    direita_x= int(tadest["di"][0])
    direita_y= int(tadest["di"][1])
    if (esquerda_X < int(tadponto[0]) < direita_x):
        if (esquerda_y > int(tadponto[1]) > direita_y):
            return True
    return False


    

