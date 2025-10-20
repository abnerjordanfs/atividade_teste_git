#1.Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dicionario_pessoas = [  {'nome':'helio', 'idade':20, 'cidade': 'russas'},
                        {'nome':'alfred', 'idade':44, 'cidade': 'manchester'},
                        {'nome':'clarck', 'idade':30, 'cidade': 'metropolis'}]

def consulta_dicionario():
    for i in dicionario_pessoas:
        for chave, valor in i.items():
            print(f"{chave.ljust(10)}: {valor}")
        print("----")

#2.Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

def muda_dicionario_nome():
    nome_para_alterar = input('qual o nome do dicionario q vc quer alterar: ')
    novo_nome = input('digite o novo nome: ')
    nome_encontrado = False
    for i in dicionario_pessoas:
        if i['nome'] == nome_para_alterar:
            i['nome'] = novo_nome
            nome_encontrado = True
    if nome_encontrado == False:
        print('nome não encontrado.') 

def muda_dicionario():
    nome = input('digite o nome da lista vc quer alterar as informações: ')
    quero_alterar = input('digite oq na lista vc quer alterar (idade/cidade): ')
    for i in dicionario_pessoas:
        if i['nome'] == nome:
            atualizacao = input(f'digite  a {quero_alterar} nova: ')
            i[f'{quero_alterar}'] = atualizacao

def adiciona_profissao():
    nome = input('digite o nome de quem você quer adicionar a profisão: ')
    profissao = input('digite qual a profissão: ')
    verifica_nome = False
    for i in dicionario_pessoas:
        if i['nome'] == nome:
            i['profissao'] = profissao
            verifica_nome = True
    if verifica_nome == False:
        print('nome não encontrado')

#muda_dicionario_nome()
#muda_dicionario()
#adiciona_profissao()
consulta_dicionario()

#3.Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados ={x: x**2 for x in range(1,6)}
def mostra_quadrados():
    for chave,valor in numeros_quadrados.items():
        print(f'o quadrado de {chave} é {valor}')
    print('')
mostra_quadrados()

#4.Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
def verifica_chave():
    chave = input('digite o nome da chave para ver se existe: ')
    chave_encontrada = False
    for i in dicionario_pessoas:
        for chave_atual in i.keys():
            if chave == chave_atual:
                chave_encontrada = True
    if chave_encontrada == False:
        print('não foi encontrado')
    else:
        print(f'a chave {chave} existe ')
#verifica_chave()

#5.Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
def conta_palavra():
    frase = input('digite uma frase: ')
    palavras = frase.split()
    conta_palavras = {}
    for palavra in palavras:
        if palavra in conta_palavras:
            conta_palavras[palavra] += 1
        else:
            conta_palavras[palavra] = 1
    for palavra,contagem in conta_palavras.items():
        print(f'{palavra.ljust(10)}: {contagem}')

conta_palavra()