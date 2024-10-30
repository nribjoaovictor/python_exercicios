import vizinhos as v
def main():
    amount_lines=int(input())
    amount_columns=int(input())
    spectrum_min=int(input())
    spectrum_max=int(input())
    matriz_main=v.geramatriz(amount_lines,amount_columns,spectrum_min,spectrum_max)
    print_main=v.f_print(matriz_main)
    position_element_line=int(input())
    position_element_columns=int(input())
    print(matriz_main[position_element_line][position_element_columns])
    print(v.f_vizinhos(matriz_main,position_element_line,position_element_columns))
main()
