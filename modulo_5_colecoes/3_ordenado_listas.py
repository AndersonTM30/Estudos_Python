import random

tamanho = 150
valor_minimo = 1
valor_maximo = 150

valores = [random.randint(valor_minimo, valor_maximo) for _ in range(tamanho)]
print(valores)
# Ordenando a lista
valores.sort()
print(valores)

# Ordena de forma decrescente
valores.sort(reverse=True)
print(valores)

# Reverte a ordem
valores.reverse()
print(valores)