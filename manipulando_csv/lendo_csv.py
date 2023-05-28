# https://dados.gov.br/dataset

# Forma não ideal
# with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
#     dados = arquivo.read()
#     # print(type(dados))
#     dados = dados.split(',')[2:]
#     print(dados)

# Forma Reader

from csv import reader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    dados = reader(arquivo, delimiter=';')
    next(dados)#pula o cabeçalho
    for linha in dados:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')
print('==========================================')
# DictReader
from csv import DictReader
with open('lutadores.csv','r', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        sql = f'INSERT INTO lutadores (nome, pais, altura) VALUES ("{linha["Nome"]}", "{linha["País"]}", {linha["Altura (em cm)"]})'
        print(sql)