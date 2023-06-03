from itertools import zip_longest

a_lista = ['A', 'B','C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5]

for a,b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]

for produto, preco in zip(produtos, precos):
    print(f'Produto {produto} no valor de {preco}')

titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Título: {titulo} - Descrição: {descricao}')

"""
Desafio 1 - Usando as listas abaixo:
    produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
    precos = ['R$500,00', 'R$1500,00', 'R$2700', 'R$5000,00']
Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, por favor, criar uma mensagem que diz o nome e o valor do porudot, como a mensagem abaixo:
    produto: Produto 1 encontrado no valor de R$500,00
"""
produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700', 'R$5000,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto; {produto} encontrado no valor de {preco}')