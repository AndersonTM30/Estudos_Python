# Criar listas com map
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

nomes = ['Larissa', 'Rafael', 'Marcos', 'John']

def aprovar_pessoa(nome):
    return nome + ' Aprovado'

print(list(map(aprovar_pessoa, nomes)))