# Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar 
# relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba 
# cada cliente.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

print(f'lista de clientes')
for cliente in clientes:
    print(f'nome: {cliente}')

# André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os 
# testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
contador = 0

while contador < 10:
    contador +=1
    print("Processando dados...")

# Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, 
# como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a 
# mensagem seja exibida 5 vezes.

for i in range(5):
    print('bem vindo buscante')

# Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de 
# calcular a soma total desses produtos para entender o desempenho financeiro semanal.
valores = [10, 20, 30, 40, 50]

soma = 0
for valor in valores:
    soma +=  valor
print(f'soma total: {soma}')

# Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos.
# Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i in projetos:
    if i == None:
        print('projeto ausente')
        continue
    print(i)

# Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>"
# assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a
# busca, sem verificar os livros restantes.

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == 'O Hobbit':
        print(f'achei: {livro}')
        break
    
# Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve 
# exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem
# "Estoque esgotado".
estoque = 5
while estoque != 0:
    estoque -= 1
    print(f'venda realizada! estoque restante {estoque}')
print('estoque esgotado.')

# Crie um programa que utilize um laço for para exibir as seguintes mensagens:
# - Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
# - Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.". 
# - Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
for i in range(10,0,-1):
    if i % 2 == 0:
        print(f'Faltam apenas {i} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {i} segundos restantes.')
print('Aproveite a promoção agora!')

# Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato:
# "Livro disponível: ".
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]
for livro in livros:
    if livro['estoque'] > 0:
        print(f"livro disponível: {livro['nome']}")

# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram
# um nome de usuário e uma senha válidos. As regras são as seguintes:
#
# - O nome de usuário deve ter pelo menos 5 caracteres.
# - A senha deve ter pelo menos 8 caracteres.
#
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o 
# usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".
while True:

    usuario = input('digite seu nome de usuario: ')
    senha = input('digite sua senha: ')
    if  len(usuario) < 5:
        print('usuario deve ter pelo menos 5 caracteres. Tente novamente\n')
        continue
    if  len(senha) < 8:
        print('sua senha deve ter pelo menos 8 caracteres. tente novamente\n')
        continue
    print('cadastro realizado com sucesso.')
    break
