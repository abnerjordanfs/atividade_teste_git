# atividade alura hora da pratica: condicionais
#1.Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else ara determinar se o número é par ou ímpar.
def verifica_par_ou_impar(numero):
    if numero % 2 == 0:
        print('número par')
    else:
        print('número é ímpar')

numero = int(input('digite o número para saber se é par ou ímpar: '))
verifica_par_ou_impar(numero)

#2.pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos; Adolescente: 13 a 18 anos; Adulto: acima de 18 anos.

def verifica_idade(idade):
    if idade >= 0 and idade <= 12:
        print('você é uma cirança ')
    elif idade >12 and idade<= 18:
        print('você é um adolescente ')
    elif idade > 18:
        print('você é adulto ')
    else:
        print('idade invalida')
idade = int(input('digite quantos anos você tem: '))
verifica_idade(idade)

#3.Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
def verifica_user_e_senha(usuario,senha):
    if usuario == usuario_certo and senha == senha_certa:
        print('autenticação validada')
    else:
        print('usuario ou senha incorretas tente novamente')
usuario_certo = 'abner'
senha_certa = 'senha'

user_name = input('digite seu nome de usuario: ')
senha = input('digite a sua senha de usuario: ')

verifica_user_e_senha(user_name,senha)

#4.Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.
def verifica_quadrante(x,y):
    if x > 0 and y > 0:
        print('esta no primeiro quadrante')
    elif x < 0 and y > 0:
        print('esta no segundo quadrante')
    elif x < 0 and y < 0:
        print('esta no terceiro quadrante')
    elif x > 0 and y < 0:
        print('esta no quarto quadrante')
    else:
        print('esta no ponto de origem')
        
ponto_x = int(input('digite o número do ponto X: '))
ponto_y = int(input('digite o número do ponto Y: '))
verifica_quadrante(ponto_x,ponto_y)