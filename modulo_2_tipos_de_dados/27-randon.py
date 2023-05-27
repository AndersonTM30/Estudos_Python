# Valores aleatórios com random
import random

print(random.random())

print(random.uniform(4, 12))

print(random.randint(4, 12))

lista = ['Anderson', 'Antero', 'Marcyo', 'Alisson', 'Matheus']

print(f"Próximo da lista: {random.choice(lista)}")

cartas = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']

print(cartas)
print(random.shuffle(cartas))
print(cartas)

# Desafio 1
# Você quer simular o opção de jogar uma moeda e resultar em cara ou coroa. Jogue as opções dentru de um lista e depois crie um programa que simule o jogo.

cara_ou_coroa = ['cara', 'coroa']
print(f"O resultado do jogo é: {random.choice(cara_ou_coroa)}")

# Desafio 2
#Você quer fazer um sorteio entre 5 nomes em uma lista de nomes, crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela.

nomes = ['Anderson', 'Antero', 'Marcyo', 'Alisson', 'Matheus']
print(f"O sorteado foi: {random.choice(nomes)}")

# Desafio 3
# Você quer escolher aleatóriamente um número entre 10 e 100 na tela.

print(random.randint(10, 100))