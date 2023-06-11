import shutil, os

arquivo_backup = ['notas.pdf','registros.txt']

arquivo_foto = ['foto1.jpg', 'foto2.jpg']

def criar_arquivos(directory, files):
    caminho = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '4_movendo_e_copiando_arquivos' + os.sep )

    os.makedirs(f'{caminho}/{directory}')

    caminho = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '4_movendo_e_copiando_arquivos' + os.sep + directory)

    for file in files:
        with open(f'{caminho}/{file}', 'w', encoding='utf-8') as arquivo:
            pass

# criar_arquivos('backup', arquivo_backup)
# criar_arquivos('fotos', arquivo_foto)

nome_pasta = 'backup'
nome_pasta_dest = 'fotos'

pasta_origem = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '4_movendo_e_copiando_arquivos' + os.sep + nome_pasta)

pasta_destino = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '4_movendo_e_copiando_arquivos' + os.sep + nome_pasta_dest)

shutil.copy2(src=pasta_origem, dst=pasta_destino) # Copia um arquivo

shutil.copytree(src=pasta_origem, dst=pasta_destino) # Copia a pasta

shutil.move(src=pasta_origem, dst=pasta_destino) # move os arquivos de uma pasta para outra

shutil.rmtree(pasta_origem) # exclui uma pasta

shutil.make_archive('backup', 'zip', pasta_origem) # compacta uma pasta

caminho = os.path.join(os.getcwd() + os.sep + 'modulo_9_manipulando_arquivos' + os.sep + '4_movendo_e_copiando_arquivos' + os.sep )
shutil.unpack_archive(f'{caminho}/backup.zip', f'{caminho}/backup_vs_code') # descompacta os arquivos em uma pasta