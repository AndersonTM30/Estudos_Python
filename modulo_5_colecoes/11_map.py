# Map é utilizado para cirar novas listas, é composto por uma função e a coleção que vai percorre e criar uma nova.
# O Map não consegue retornar os dados na tela, ideal é converter o map para uma lista com a função list()
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    return nome + ' Aprovado'

lista_aprovados = list(map(aprovar_pessoa, nomes))
for indice, pessoa in enumerate(lista_aprovados, 1):
    print(f'Nº {indice} - Nome: {pessoa}')

