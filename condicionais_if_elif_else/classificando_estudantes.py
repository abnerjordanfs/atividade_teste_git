# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, 
# exiba a situação do aluno.
# - Média >= 7: Aprovado
# - 5 <= Média < 7: 
# - < 5: Reprovado

def media():
    while True:
        try:
            nota1 = float(input('digite a primeira nota: '))
            nota2 = float(input('digite a segunda nota: '))
            nota3 = float(input('digite a terceira nota: '))
            if 0 >= nota1 <=10 and 0 >= nota2 <=10 and 0 >= nota3 <=10:
                return (nota1+nota2+nota3)/3
            else:
                print('valores inválidos tenjte novamente')
        except: 
            print('error apenas numeros são aceitos tente novamente.. ')
            print('')


def verifica_aprovacao(media):
    if media >= 7: 
        return 'aprovado'
    elif media >= 5 and media < 7:
        return 'recuperação'
    elif media < 5:
        return 'reprovado'

print(verifica_aprovacao(media()))

