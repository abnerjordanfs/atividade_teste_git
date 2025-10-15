#1.Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C.
# Ele quer um programa que receba a temperatura atual como entrada e, 
# se necessário,exiba uma mensagem de alerta.

temperatura = float(input('digite a temperatura atual em Celcius: '))

if temperatura > 25:
    print ('ALERTA, temperatura acima do limite')
else:
    print('tudo tranquilo s2')