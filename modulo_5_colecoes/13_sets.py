# O set é uma lista dinâmica que não aceita informações repetidas
numeros = [2, 2, 5, 8]
frutas = {'maçã', 'uva', 'banana', 'maçã', 'morango'}

#convertendo as listas para sets
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

set_numeros.add(10)
print(set_numeros)

numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]

a = set(numeros1)
b = set(numeros2)
# retorna apenas um conjunto com os números diferentes nas duas listas
print(f'Retornando os números diferentes: {a.symmetric_difference(b)}')
# Esta função verificar quais os valores estão iguais nas duas listas
print(f'Retorna a interceção de um conjunto de listas: {a.intersection(b)}')
# Esta função une as duas listas removendo os valores duplicados
print(f'Une os dois conjutos tirando os valores repetidos: {a.union(b)}')