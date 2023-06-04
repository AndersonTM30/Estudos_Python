# A função range gera um valor no array
print(type(range(30)))

for numero in range(10, 30, 2):
    print(numero)
# Pode ser utilizado para criar listas mais rapidamente
resultado = list(range(0, 201, 10))
print(resultado)