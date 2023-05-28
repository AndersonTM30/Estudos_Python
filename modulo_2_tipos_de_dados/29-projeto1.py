from datetime import datetime
import random


print('Bem Vindo ao Sistema S')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
data_nascimento = datetime.strptime(input('Digite a sua data de nascimento: '), '%d/%m/%Y')
registro = datetime.now().strftime('%d/%m/%Y')
cartoes = ['R$50,00', 'R$250,00', 'R$120,00'] 
lista_cartoes = random.choice(cartoes)

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {registro}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {lista_cartoes}')