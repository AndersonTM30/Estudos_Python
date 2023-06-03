#listas
precos = [10, 20, 30, 40, 50, 60 , 70, 80, 90, 100, 200, 300, 400, 500, 600]
print(precos[0]) #indice
print(precos[precos.index(100)]) # Faz um filtro do valor pelo índice, passando o valor que deseja encontrar no íncide
# Listas no python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 'Olá', True, 2.0]
print(itens[3])
# Maneiras diferentes de gerar uma lista:
    #Multiplicação de valores (repetição)
lista_de_novas = [9] * 10
lista_de_testes = ['Teste'] * 10
print(lista_de_novas)
print(lista_de_testes)
# Usando gerador Range(Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)
# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))
# Lista de lista (matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])

# Desafio 1 - Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ela na tela
print('=========================== Desafios ==============================')
objetos = ['Notebook', 'Celular', 'Chave']
print(f'Objetos que uso no meu dia a dia: {objetos}')
# Desafio 2 - Usando apenas uma linha de código, crie uma lista de 10 até 131
lista_de_numeros = list(range(10, 132))
print(lista_de_numeros)
# Desafio 3 - Imprima na tela o resulta da combinação da lista do disafio1 e desafio 2
print(objetos + lista_de_numeros)
"""
Desafio 4 - Crie uma lista de listas(matriz) que tenha os noems dos 3 objetos que você mais usa durante o dia,
mas agora dentro de cada item você vai colocar uma informação extra, coloque o valor em reais desse objeto
também e imprima ele na tela
"""
matriz_de_objetos = [['Notebook', 'R$3.500,00'], ['Celular', 'R$1.200,00'], ['Chave', 'R$30,00']]
print(matriz_de_objetos[0])
print(matriz_de_objetos[1])
print(matriz_de_objetos[2])