"""
def nome_da_funcao(parametros):
    comandos
"""

def bemvindo(nome):
    print(f'Bem-vindo! {nome}')

bemvindo('Anderson')

# Função com valor padrão

def apresentar_lugar(lugar='nossa loja'):
    print(f'Conheça {lugar}')

apresentar_lugar()

"""
Desafio 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome 
de alguém e dá boas vindas para essa pessoa
"""
def gerar_nome_completo(nome, sobrenome):
    print(f'Seja Bem-Vindo {nome} {sobrenome}')

gerar_nome_completo('Anderson', 'Ferreira')


"""
Crie uma função chamada calcular_valores que recebe 2 parâmetros, o primeiro é o preço de um produto e o
segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve
exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
"""

def calcular_valores(preco_produto, quantidade=2):
    total = float(preco_produto * quantidade)
    print(f'O cálculo {preco_produto} * {quantidade} = {total}')

calcular_valores(50)