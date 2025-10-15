# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
# O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições.
# - O valor da renda mensal precisa ser maior que R$ 2.000,00.
# - O valor da parcela não pode ultrapassar 30% da renda.

def aprova_emprestimo():
    renda = float(input('digite o valor sua renda mensal: '))
    parcela = float(input('digite o valor das parcelas que deseja pagar: '))
    
    if renda > 2000 and parcela <= 0.3* renda:
        print('aprovado')
    elif renda <= 2000:
        print('emprestimo negado, renda muito baixa')
    else:
        print('parcela acima de 30% do valor da renda')

aprova_emprestimo()