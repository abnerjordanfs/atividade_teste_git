# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com 
# base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e 
# retorne à idade correspondente.
def calcula_idade():
    nascimento = int(input('digite que ano vc nasceu: '))
    return 2025 - nascimento
#print(calcula_idade())

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
def conta_caracteres(palavra):
    x = len(palavra)
    print(f'a palavra {palavra} tem {x} caracteres') 
#conta_caracteres(input('digite uma palavra: '))

# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar 
# um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa
# a plataforma. O sistema deverá ter a seguinte regra:
# - Se for antes das 12h, exibir "Bom dia"
# - Entre 12h e 18h, exibir "Boa tarde"
# - Após 18h, exibir "Boa noite"
def saudacao(hora):
    if hora < 12:
        print('bom dia')
    elif hora > 18:
        print('boa noite')
    else:
        print('boa tarde.')
#saudacao(int(input('digite q horas são: ')))

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções,
# uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números 
# de telefone são inteiros:

def converte_para_inteiro(lista):
    lista_inteiros = []
    for i in lista:
        lista_inteiros.append(int(i))
    return lista_inteiros

def verifica_lista(lista):
    for i in lista:
        if type(i) != int:
            return print('error a lista não é totalmente composta de números inteiros')
        else:
            return print('Todos os números foram convertidos corretamente! ')

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
lista_convertida = converte_para_inteiro(telefones)
#verifica_lista(lista_convertida)

# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas
# em uma única linha separadas por espaços. 
# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

def somatorio_do_dia(): 
    valores = input('Digite os valores das vendas: ')
    lista_velores = map(float,(valores.split()))
    soma = sum(lista_velores)
    return print('O total de vendas foi:',soma)

#somatorio_do_dia()

# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores 
# pares de uma lista de números informada pelo usuário.
# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
def separa_pares():
    lista_numeros = input('digite os números separados por espaço: ').split()
    lista_numeros = [int(i) for i in lista_numeros]
    lista_pares = list(filter(lambda x: x % 2 == 0,lista_numeros))
    print(lista_pares)
#separa_pares()

# Crie um programa que junte as listas e exiba o resultado no formato produto: 
def junta_produtos():
    produtos = input('Digite os produtos separados por vírgula: ').split(',')
    precos = [float(i) for i in (input('Digite os preços separados por vírgula: ').split(','))]
    juntos = list(zip(produtos,precos))
    for produto,preco in juntos:
        print(f'{produto.strip()}: {preco}')
#junta_produtos()

# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático 
# escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

def calcula_lambda():
    x1 = float(input('digite o primeiro numero: '))
    x2 = float(input('digite o segundo numero: '))
    operacao = input('escolha a operação ( + | - | * | / ): ')
    match operacao:
        case '+':
            print('resultado: ',(lambda a,b: a+b)(x1,x2))
        case '-':
            print('resultado: ',(lambda a,b: a-b)(x1,x2))
        case '*':
            print('resultado: ',(lambda a,b: a*b)(x1,x2))
        case '/':
            print('resultado: ',(lambda a,b: a/b)(x1,x2))
        case _ :
            print('operacao incorreta')
#calcula_lambda()

# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de 
# desconto sobre os valores das compras.
# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com 
# um desconto fixo definido pelo usuário.
def desconta(x):
    def calcula_valor(valor):
        return valor - (valor * (x/100))
    return calcula_valor

def calcula_valor_com_desconto():
    percentual  = float(input('percentual de desconto: '))
    calcular_preco_final = desconta(percentual)
    valor = float(input('o valor da compra é: '))
    print(f'valor final com desconto é :{calcular_preco_final(valor)}')
#calcula_valor_com_desconto()

# Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro.
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário. 
# Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
def recursivo_somatorio(n):
    if n == 1:
        return 1
    else:
        return n + recursivo_somatorio(n-1)
#print('valor do somatorio: ',recursivo_somatorio(6))


