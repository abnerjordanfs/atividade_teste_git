# Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os 
# funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 
# 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma 
# mensagem informando se o acesso é permitido ou negado.
def verifica_horario_de_acesso():
    while True:
        try:
            hora_atual = int(input('digite q horas são: '))
            if hora_atual > 8 and hora_atual <= 18:
                return print('acesso concedido')
            else:
                return print('acesso negado')
        except:
            print('valor deve conter apenas as horas entre 00 a 24')

verifica_horario_de_acesso()