# Arrays no python armazenam dados apenas do mesmo tipo

from array import array

numeros = array('i', [1, 2, 3, 4 ,5])
print(numeros)
numeros.append(10)
print(f'Adicionando item no array {numeros}')
numeros.insert(5, 200)
print(f'Adiciona um item no array em uma posição específica {numeros}')
numeros.pop(1)
print(f'Remove um item do array na posição específica {numeros}')
numeros.remove(5)
print(f'Remove um item do array no valor específico {numeros}')
del numeros[1]
print(f'Remove um ao mais itens pelo index {numeros}')