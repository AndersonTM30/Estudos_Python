""" 
Escreva um programa que solicita ao usuário que digite um número inteiro e, em seguida, verifica se o número é par ou ímpar. Se o número for par, o programa deve imprimir "O número é par". Caso contrário, o programa deve imprimir "O número é ímpar" 
"""
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')