#1.Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10; Lista com quatro nomes; Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes =['abner','joão','ronaldo','hellen']
lista_ano_nacimento_e_atual = [1998,2025]

#2. Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for itens in lista_numeros:
    print(itens)
print('')

#3. Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for i in range(1,11) :
    if i % 2 != 0:
        soma += i
print(soma)
print('')

#4. Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
x = 10
for numeros in range(1,11):
    print(x)
    x -=1
print('')

#5.Solicite ao usuário um número e, em seguida, utilize um loop for para 
# imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input('digite um número e te direi a tabuada dele: '))
for i in range(1,11):
    print(f'{numero_tabuada} x {i} = {numero_tabuada*i}')
print('')

#6.Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com possíveis exceções.
lista_de_numeros = [10,4,7,3]
try:
    soma_lista = 0
    for i in lista_de_numeros:
        soma_lista += i
    print(soma_lista)
    print('')
except:
    print('error')

#7.Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_da_media = [6,7,8]
soma_media = 0
try:
    for i in lista_da_media:
        soma_media += i
    print(soma_media/len(lista_da_media))
except:
    print('error na media')