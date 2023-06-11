import os

caminho_pasta = os.chdir('modulo_9_manipulando_arquivos' + os.sep + '1_conceito_de_os' + os.sep + 'desafio_arquivos')
print(f'Arquivos da pasta: {os.listdir(caminho_pasta)}')

print(f'Caminho da pasta atual: {os.getcwd()}')

caminho_sub_pasta = os.chdir('desafios_texto')

print(f'Arquivos da pasta: {os.listdir()}')

print(f'Caminho da pasta atual: {os.getcwd()}')

volta_um_diretorio = os.chdir('..')

print(f'Caminho da pasta atual: {os.getcwd()}')

volta_um_diretorio = os.chdir('..')

print(f'Caminho da pasta atual: {os.getcwd()}')
