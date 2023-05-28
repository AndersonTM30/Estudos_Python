"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha
"""

"""
writer() -> Gera um objeto para que possamos escrever em uma arquivo CSV. Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.
"""

# from csv import writer

# with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
#     escritor = writer(arquivo, delimiter=';')
#     filme = None
#     escritor.writerow(['Título', 'Gênero', 'Duração'])
#     while filme != 'sair':
#         filme = input('Nome do filme: ')
#         if filme != 'sair':
#             genero = input('Gênero: ')
#             duracao = input('Duração: ')
#             escritor.writerow([filme, genero, duracao])


from csv import DictWriter

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor = DictWriter(arquivo, fieldnames=['titulo', 'genero', 'duracao'])
    escritor.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Nome do filme: ')
        if filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração: ')
            escritor.writerow({'titulo': filme, 'genero': genero, 'duracao': duracao})