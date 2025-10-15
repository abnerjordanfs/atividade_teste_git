# Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar.
# Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba 
# um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

def verifica_par_ou_impar():
    numero = int(input('digite um numero pra saber se é par ou impar: '))
    if numero%2 == 0:
        print('é par')
    else: 
        print('é ímpar')

verifica_par_ou_impar()