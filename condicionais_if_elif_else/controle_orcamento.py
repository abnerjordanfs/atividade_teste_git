# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu 
# um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas 
# despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o 
# limite ou ainda está dentro do orçamento.

def despesas_do_mes():
    soma = 0
    while True:
        try:
            soma += float(input('digite o quanto gastou: '))
            print('ainda tem mais gastos?')
            resposta = input('digite sim ou não:')
            print('')
            if resposta.lower() == 'não':
                return soma
        except ValueError:
            print('erro digite apenas números válidos')

def limite_orcamento():
    if despesas_do_mes() > 3000:
        print('orçamento ultrapassado')
    else:
        print('tudo dentro do orçamento')
limite_orcamento()