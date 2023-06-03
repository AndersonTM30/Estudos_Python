# Criação de tuplas
sites = ('youtube.com','facebook.com','instagram.com')
valores = (23, 24, 25)
print(sites)
print(valores)

print('============================')
# União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)

# Acessando o valor de uma tupla pelo índice
print(dados_do_sistema[2])

# Tuplas também são dinâmicas
lista = ('Anderson', 31, 1.70, True, None)
print(lista)