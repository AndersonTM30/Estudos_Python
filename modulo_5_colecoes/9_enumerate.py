# Com a função Enumerate podemos saber qual o índice estamos iterando no array. ele retorna dois valores, o índice e o valor
for indice, numero in enumerate(range(1,11), 1):
    print(f'Índice: {indice} - Valor: {numero}')

nomes = ['nome 1', 'nome 2', 'nome 3', 'nome 4', 'nome 5']

for indice, nome in enumerate(nomes, 1):
    print(f'Índice: {indice} - Nome: {nome}')
    if indice == 3:
        print('Já temos 3 pessoas registradas!')

"""
Desafio - Itere sobre a lista abaixo exibindo o número do índice + nome da fruta. Porém quando o índice for 3 exiva 'Nº índice + nome da fruta EM PROMOÇÃO'
"""
frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, item in enumerate(frutas, 1):
    if indice == 3:
        print(f'Nº {indice} - Fruta: {item} - EM PROMOÇÃO')
    else:
        print(f'Nº {indice} - Fruta: {item}')
