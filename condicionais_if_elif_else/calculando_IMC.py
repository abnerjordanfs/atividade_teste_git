# Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e 
# fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e 
# exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
# Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: 
# IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está 
# abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
def coleta_peso_altura():
    try:
        peso = float(input('digite seu peso em KG: '))
        altura = float(input('digite sua altura em metros: '))
        return peso,altura
    except ValueError:
            print('valores não correspondentes')

def calcula_imc(peso,altura):
    imc = round(peso/(altura**2),2)
    print(f'seu IMC é: {imc}')
    return imc

def verifica_imc(imc):
    if imc < 18.5:
        print('você esta abaixo do peso: ')
    elif imc > 25:
        print('você esta acima do peso')
    else: 
        print('peso normal')

peso,altura = coleta_peso_altura()
imc = calcula_imc(peso,altura)
verifica_imc(imc)