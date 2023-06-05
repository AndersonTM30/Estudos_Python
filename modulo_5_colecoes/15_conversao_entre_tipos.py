# Conversão entre tipos

idade = input('Digite a sua idade: ')
print(int(idade) > 17)

ano_publicacao = 2020

print('Este livro foi criado em ' + str(ano_publicacao))

altura = input('Qual é a altura da parede? ')
print(float(altura) > 2.50)

# Conversão entre coleções
saudacao = 'Hello!'
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(30)))

numeros = [10, 20, 30, 40, 50]

print(set(numeros))
print(tuple(numeros))
print(type(numeros))