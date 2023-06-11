from csv import DictReader, DictWriter

#Ler um arquivo csv
def lendo_csv():
    with open('dados.csv') as arquivo:
        dados = DictReader(arquivo, delimiter=';')
        for dado in dados:
            print(f'{dado["data"]} - {dado["valor"]}')

def criar_csv():
    with open('computadores.csv', 'w', newline='', encoding='utf-8') as arquivo:
        cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
        csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()# Cria o cabeçalho na planilha
        csv_writer.writerow({# Cria as linhas do cabeçalho
            'Marca': 'Asus',
            'Preço': 2500,
            'Ano de Lançamento': 2012
        }),

        csv_writer.writerow({
            'Marca': 'Mac',
            'Preço': 7000,
            'Ano de Lançamento': 2015
        }),

        csv_writer.writerow({
            'Marca': 'Dell',
            'Preço': 4500,
            'Ano de Lançamento': 2014
        })
# criar_csv()

# alterar um arquivo csv
def editando_csv(file):
    with open(file, 'r', newline='', encoding='utf-8') as arquivo_original:
        dados_originais = DictReader(arquivo_original)
        computadores = list(dados_originais)
        with open('computadores_v2.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
            cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
            csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
            csv_writer.writeheader()
            for computador in computadores:
                csv_writer.writerow({
                    'Marca': computador['Marca'],
                    'Preço': 'R$' + computador['Preço'],
                    'Ano de Lançamento': computador['Ano de Lançamento']
                })

# editando_csv('computadores.csv')

def criar_csv_pessoa():
    with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
        cabecalho = ['nome', 'idade', 'altura']
        csv_write = DictWriter(arquivo, fieldnames=cabecalho)
        csv_write.writeheader()
        csv_write.writerow({
            'nome': 'Mark',
            'idade': 25,
            'altura': 170
        })
        csv_write.writerow({
            'nome': 'Carol',
            'idade': 19,
            'altura': 160
        })
        csv_write.writerow({
            'nome': 'Robert',
            'idade': 65,
            'altura': 175
        })

criar_csv_pessoa()

def editar_csv_pessoa(file):
    with open(file, 'r', newline='', encoding='utf-8') as arquivo_original:
        dados_originais = DictReader(arquivo_original)
        pessoas = list(dados_originais)
        with open(file, 'w', newline='', encoding='utf-8') as novo_arquivo:
            cabecalho = ['nome', 'idade', 'altura']
            csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
            csv_writer.writeheader()
            for pessoa in pessoas:
                csv_writer.writerow({
                    'nome': pessoa['nome'],
                    'idade': pessoa['idade'],
                    'altura': pessoa['altura'] + 'cm'
                })

editar_csv_pessoa('pessoas.csv')