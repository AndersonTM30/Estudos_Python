import os

print(os.name)# Verifica qual o sistema operacional
print(os.listdir()) # Verifica os arquivos da pasta atual
print(os.sep) # Verifica o separador de diretórios do sistema operacional
print(os.getcwd()) # Mostra o caminho do diretório da pasta atual
print(os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '1_conceito_de_os' + os.sep + 'documentos' + os.sep + 'musica.mp3')) # acessa o arquivo no caminho informado

caminho_senha = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '1_conceito_de_os' + os.sep + 'senhas.txt')

print(os.path.dirname(caminho_senha)) # obter o diretório de um path
print(os.path.basename(caminho_senha)) # obter arquivo de um path

print(os.path.exists(os.getcwd() + os.sep + 'documentos')) # Verifica se um diretório existe

os.chdir('modulo_9_manipulando_arquivos' + os.sep + '1_conceito_de_os' + os.sep + 'documentos') # Navega para uma pasta 
print(os.getcwd())
os.chdir('..') # volta uma pasta
print(os.getcwd())
