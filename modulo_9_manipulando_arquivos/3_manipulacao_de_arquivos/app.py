"""
Como criar e modificar arquivos:
'r' - Usado somente para ler algo
'w' - Usado somente para escrever algo
'r+' - Usado para ler e escrever algo
'a' - Usado para acrescentar algo
"""
import os
caminho = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '3_manipulacao_de_arquivos' + os.sep )

# with open(f'{caminho}/nomes.txt', 'w') as arquivo:
#     arquivo.write('Celular 1')

# with open(f"{caminho}/celulares.txt", 'a', newline='') as arquivo:
#     for line in range(1, 11):
#         arquivo.write(f'Celular {line}' + os.linesep)

# nomes = ['Lucas', 'Carol', 'Jeff', 'Douglas']
# with open(f"{caminho}/nomes.txt", 'a', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)

# # para escrever números em um arquivo de texto precisa converter para string antes
# numeros = [1, 2, 3, 4, 5, 6]
# with open(f"{caminho}/numeros.txt", 'a', newline='') as arquivo:
#     for numero in numeros:
#         arquivo.write(str(numero) + os.linesep)

# with open(f'{caminho}/nomes.txt', 'r') as arquivo: # lendo arquivo
#     for linha in arquivo:
#         print(linha)

# with open(f'{caminho}/numeros.txt', 'r+') as arquivo: # lendo e escrevendo ao mesmo tempo
#     for linha in arquivo:
#         print(linha)
#     arquivo.write('9000')

"""
Desafio - Manipulação de Arquivos
"""
frutas = ['Banana', 'Laranja', 'Mamão', 'Maçã', 'Acerola']
cores = ['Azul', 'Vermelho', 'Verde', 'Amarelo', 'Preto']
linguagens = ['Java', 'Javascript', 'C', 'PHP', 'Python']

with open(f'{caminho}/frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for linha in frutas:
        arquivo.write(linha + os.linesep)

with open(f'{caminho}/frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open(f'{caminho}/frutas.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)

with open(f'{caminho}/Tops 5 Linguagens.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)
        print(linguagem)

arquivos = ['musia.mp3', 'foto.jpg', 'senhas.txt', 'relatório.pdf']

for arquivo in arquivos:
    with open(f'{caminho}/{arquivo}', 'w', encoding='utf-8') as arquivo:
       pass