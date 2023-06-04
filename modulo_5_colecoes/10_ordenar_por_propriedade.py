from operator import itemgetter
pessoas = [
    {'nome': 'Charlie', 'idade': 20, 'nivel_acesso': 1},
    {'nome': 'Alice', 'idade': 25, 'nivel_acesso': 2},
    {'nome': 'Bob', 'idade': 30, 'nivel_acesso': 3},
    {'nome': 'Tomas', 'idade': 30, 'nivel_acesso': 4}
]

pessoas.sort(key=lambda pessoa: pessoa['nome'])
print(pessoas)

pessoas.append(dict(nome='Anderson', idade=31, nivel_acesso=2))

pessoas.sort(key=itemgetter('nome'))

print(pessoas)

# Ordenando tuplas
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550),
    ('Bolsa', 250),
    ('Sapato', 200)
]

produtos.sort(key=lambda produto: produto[1], reverse=True)
print(produtos)

produtos.sort(key=itemgetter(0))
print(produtos)

matriz = [[5, 10], [15, 21], [1, 5]]

matriz.sort(key=itemgetter(1))
print(matriz)

matriz.sort(key=lambda mat: mat[0], reverse=True)
print(matriz)

# Desafio 1 - Ordene a lista de produtos abaixo pelo preço em ordem crescente

produtos = [
    {
        'nome': 'Celular',
        'preco': 1500
    },
    {
        'nome': 'Monitor',
        'preco': 500
    },
    {
        'nome': 'Microfone',
        'preco': 300
    },
]

produtos.sort(key=itemgetter('preco'))
print(produtos)

# Desafio 2 - ordene em ordem decrescente a lisata de equipamento_filmagem por valor do equipamento

equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Desafio 3 - Ordene em ordem crescente a cotacao_moedas com base no valor da moeda

cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)