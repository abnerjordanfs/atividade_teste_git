# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
# - Até 100 km: R$ 10,00
# - Entre 100 km e 200 km: R$ 20,00
# - Acima de 200 km: R$ 30,00



def calcula_pedagio():
    try:
        distancia_percorrida = float(input('digite a distância percorrida em km: '))
        if distancia_percorrida <= 100:
            print('pague 10 reais')
        elif distancia_percorrida > 100 and distancia_percorrida <= 200:
            print('pague 20 reais')
        else:
            print('pague 30 reais')
    except:
        calcula_pedagio()
        
calcula_pedagio()