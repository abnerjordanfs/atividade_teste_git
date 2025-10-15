#1.Escreva um programa que receba o número de dias de três atividades e exiba o 
# tempo total do projeto.Se algum valor for negativo, mostre uma mensagem informando o erro.

try:
    a = int(input('informe os dias para atividade A: '))
    b = int(input('informe os dias para atividade B: '))
    c = int(input('informe os dias para atividade C: '))
    print(f'dias totais: {a+b+c}')
except:
    if a or b or c != int:
        print('número inteiro esperado')
    if a or b or c > 0:
        print('os dias não podem ser negativos')