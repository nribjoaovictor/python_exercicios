import tadponto as tp
import tadest as te
import read_est as re
import read_ponto as rp

def main():
    pontos=rp.chamando_arquivo("prova3_tad/bdveiculos.txt")
    estacionamento=re.chamando_arquivo("prova3_tad/bdestacionamentos.txt")
    #-----------------------------
    for empresa in estacionamento:
        print()
        print(("empresa:%s") %(te.get_empresa(empresa)))
        print(("email:%s") %(te.get_email(empresa)))
        print(("area:%.2f") %(te.area(empresa)))
        print(("perimetro:%.2f") %(te.perimetro(empresa)))
        carros=0
        for quantidade in pontos:
            est_vaga=te.pertence(empresa,quantidade)
            if est_vaga:
                carros+=1
                te.set_num_carros(empresa,carros)
        print(("carros:%d empresa:%s") %(te.get_num_carros(empresa),te.get_empresa(empresa)))
        print()
        print("----------------------------------")
main()