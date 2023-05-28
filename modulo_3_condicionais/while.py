tentativas = 0

while tentativas < 3:
    print('Tente novamente!')
    tentativas += 1

senha = ''

while senha != '123456':
    senha = input('Digite a senha: ')
print('Seja bem vindo!')

# Recebe o nome do usuário

nome = ''
while nome == '':
    nome = input('Digite o seu nome: ')
print(f'Bem-vindo {nome}')

# Por do sol
horario = 1

while horario <= 17:
    print(f'Agora são {horario} horas')
    horario += 1
print('Hora de ir ver o por do sol')

contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

# Desafio
#  Crie um loop while que irá contar e imprimir no console de 1 até 120
count = 1
while count <= 120:
    print(count)
    count += 1
# Desafio 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá
#  permitir o programa continuar caso ele digite a senha 'secreto'
password = ''
while password != 'secreto':
    password = input('Digite a senha: ')
# Desafio 3 - Crie um loop while que irá contar e imprimir no console de 100 até 1.
count = 100
while count >= 1:
    print(count)
    count -= 1