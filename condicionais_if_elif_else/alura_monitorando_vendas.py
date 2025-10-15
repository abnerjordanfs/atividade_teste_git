#.Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas 
# no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
# Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando 
# qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

produtos = [{'fruta' : 'banana','quantidade': 2},
            {'fruta' : 'maçã', 'quantidade': 2},
            {'fruta' : 'uva', 'quantidade' : 0}]

def quantidade_vendida():
    for produto in produtos:
        produto['quantidade'] = int(input(f"quantidade de {produto['fruta']} vendidos: "))
    print('')

def consulta_produtos():
    for produto in produtos:
        print(f"{produto['fruta'].ljust(8)} vendidas:{produto['quantidade']}")
    print('')

def compara_vendas():
    quem_vendeu_mais = []
    quantidade_maxima_vendida = 0
    print('lista dos items mais vendidos')
    for produto in produtos:
        if produto['quantidade'] > quantidade_maxima_vendida:
            quantidade_maxima_vendida = produto['quantidade']
    for produto in produtos:
        if produto['quantidade'] == quantidade_maxima_vendida:
            quem_vendeu_mais.append(produto)
    for i in quem_vendeu_mais:
        print(f"items mais vendido {i['fruta']} com: {i['quantidade']}")

quantidade_vendida()
consulta_produtos()
compara_vendas()
