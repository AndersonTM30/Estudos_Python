"""
Para funções terem argumentos dinâmicos adiciona o asterísco (*) no início do nome do argumento
"""

def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 5, b=5)