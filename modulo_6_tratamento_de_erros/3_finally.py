internet = None

try:
    print('Fazendo a conexão com a ' + internet)
except TypeError as error:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')

try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as error:
    print('Não é possível dividir por zero!')
except ValueError as error:
    print('Por favor digitar apenas números!')
finally:
    print('A operação foi cancelada!')