cnpj = '12.345.678/0001-10'
print(cnpj)
print(cnpj.split('.'))
print(cnpj.split('/'))
print(cnpj.split('-'))
print(f"{cnpj.replace('.', '').replace('/', '').replace('-', '')}")
lista = '#Java #Javascript #PHP #Python #Ruby #C #Typescript'
print(lista.split())
novaLista = lista.split('#')
print(';'.join(novaLista))

#Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1.
#Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2.
#Desafio3: Pegue o palavras' e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
#Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: "Anderson & Antero & Matheus & Marcyo & Alisson & Caio". Imprima o resultado no console.
frase1 = 'Desagio manipulação de strings'
frase2 = 'Anderson,Antero,Matheus,Marcyo,Alisson,Caio'

palavras1 = frase1.split()
print(palavras1)
palavras2 = frase2.split(',')
print(palavras2)

print(','.join(palavras1))
print(' & '.join(palavras2))