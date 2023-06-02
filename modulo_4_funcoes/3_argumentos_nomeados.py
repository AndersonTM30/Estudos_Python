
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')


# Argumentos posicionais
exibir_preco('Iphone', 5000)

# Argumentos nomeados
exibir_preco(preco=5000, nome_produto='Iphone')

# Para deixar uma função com todos os argumentos nomeados, coloca-se um asterísco (*) como primeiro argumento:

def exibir_preco2(*, nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

exibir_preco2(nome_produto='Sansung', preco=5000)

"""
Desafio - Crie uma função chamada gerar_objeto_personalizado que irá receber 3 parâmetros: cor, altura, formato. A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos. Porém ela deve serguir as seguintes regras:
    1 - O primeiro argumento deve ser posicional
    2 - Os argumentos de altura e forma precisam OBRIGATORIAMENTE serem nomeados
"""

def gerar_objeto_personalizado(cor, *, altura, formato):
    print(f'Objeto de cor {cor}, que mede {altura} metros e tem o formato {formato}')

gerar_objeto_personalizado('Azul', altura='1.70', formato='quadrado')