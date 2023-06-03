# Dicionários são representados por chave, valor
dicionario_pessoa = {'nome': 'Anderson', 'idade': 31, 'altura': 1.70}
dicionario_pessoa2 = dict(nome='Carol', idade=18, altura=1.60)
print(dicionario_pessoa)
print(dicionario_pessoa2)
# Acessando todas as chaves de um dicionário
print(dicionario_pessoa.keys())
# Acessando um valor dentro de um dicionário
print(dicionario_pessoa['nome'])
print(dicionario_pessoa2['nome'])

# Acessando os valores dentr de um dicionário
print(dicionario_pessoa.values())

# Acessando tanto a chave quanto o valor de um dicionário
print(dicionario_pessoa.items())

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item[1])