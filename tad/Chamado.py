# def new_pessoa(nome,peso,altura,idade): #retorna a estrutura de dados que vc escolhe para representar e armazenar os dados de uma pessoa

# def imc(tadpessoa): #retorna o imc da pessoa como argumento
# getNome(tadpessoa) #retorna o nome da pessoa usada como argumento
# getPeso(tadpessoa) #retorna o peso da pessoa usada como argumento
# getAltura(tadpessoa) #retorna a altura da pessoa usada como argumento
# getIdade(tadpessoa) #retorna a Idade da pessoa usada como argumento

#papel do usuário: construa uma palicação que leia um arquivo contendo, em cada linha, o nome , a idade, a altura e o peso
#de pessoas, em cada linha, os dados estão sepados por virgula, para cada pessoa lida, crie um dado tipo TADpessoa e armazene-o em uma lista

# Por ultimo, passeie pela lista interagindo com o TAdpessoa e calcule o imc de cada pessoa
# ,para cada pessoa, exiba na tela o nome, idade,peso, altura e o valor do imc apenas se a pessoa for maior.

def tadpessoa(nome,peso,altura,idade):    
    return  {'nome':nome,'peso':int(peso),'altura':float(altura),'idade':int(idade)}

def getNome(tadpessoa):
    return tadpessoa['nome']

def getPeso(tadpessoa):
    return tadpessoa['peso']

def getAltura(tadpessoa):
    return tadpessoa['altura']

def getIdade(tadpessoa):
    return tadpessoa['idade']

def maior(tadpessoa):
    return tadpessoa['idade']>=18

def imc(tadpessoa):
    imc=tadpessoa['peso']/(tadpessoa['altura']**2)
    return imc