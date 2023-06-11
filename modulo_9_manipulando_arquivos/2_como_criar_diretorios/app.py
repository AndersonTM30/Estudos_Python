import os

caminho_pasta = os.chdir('modulo_9_manipulando_arquivos' + os.sep + '2_como_criar_diretorios')

# os.mkdir('Musicas') # cria uma pasta (não pode criar a mesma pasta duas vezes)

print(os.listdir())

# os.makedirs('Videos' + os.sep + 'Ação') # cria sub pastas

# os.makedirs('Musicas' + os.sep + 'Rock')

print(os.path.isdir('Musicas')) # Verifica se a pasta já existe

# Desafio
"""
Crie um novo diretório dentro do diretório atual, chamado 'Arquivos
Em um outro comando crie um novo diretório dentro do diretório 'Arquivos' chamado 'Arquivos Musicais'
Em apenas uma linha de código crie o diretório 'Musicas, como o sub-diretório 'Rock'
"""

os.makedirs('Arquivos' + os.sep + 'Arquivos Musicais' + os.sep + 'Musicas' + os.sep + 'Rock')
