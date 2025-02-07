import tadponto
import tadest
def main():
    arquivo_est=tadest.chamando("python/prova3/bdestacionamentos.txt")
    arquivo_veiculo=tadponto.chamando_veiculo("python/prova3/bdveiculos.txt")
    for j in range(len(arquivo_veiculo)):
        for i in arquivo_veiculo:
            pontos=tadponto.new_ponto([j][i][0],[j][i][1])
            print(pontos)
            print(tadponto.get_x(pontos))
            print(tadponto.get_y(pontos))
    
    for j in arquivo_est:
        dic_1=tadest.new_est(arquivo_est[j])
        print(dic_1)
        print(tadest.get_empresa(dic_1))
        print(tadest.get_email(dic_1))
        print(tadest.get_num_carros(dic_1))
        print(tadest.area(dic_1))
        print(tadest.perimetro(dic_1))
        print(tadest.pertence(dic_1))

    if tadest.pertence(dic_1)==True:
        tadest.set_num_carros(dic_1,tadest.get_num_carros(dic_1))
    
main()