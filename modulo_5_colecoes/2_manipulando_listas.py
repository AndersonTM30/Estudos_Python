valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]
# Adiciona um item ao final da lista
valores.append(11)
print(valores)
# Unir listas
valores.extend(anos)
print(valores)
# Adicionar lista
nova_lista = valores + anos # Aqui não é altarado os valores da lista, mas sim criada uma nova lista com os novos valores
print(nova_lista)
# Inserir um item na lista na posição desejada
print(anos[2])
anos.insert(2, 2031) # Primeiro argumento é o índice e o segundo é o valor
print(anos)
#Extrair com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)
# Remover item da lista
anos.remove(2040)
del anos[1:3] # desta forma pode remover uma sequência de itens
print(anos)
# contando a ocorrência de um valor
print(valores.count(2))
# Apagar todos os itens da lista
valores.clear()
print(valores)