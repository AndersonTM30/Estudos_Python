teclado = 'Teclado'
print(f'O {teclado} tem {len(teclado)} caracterese a sua última letra é {teclado[-1]}. \nPara localizar a letra c usase a sintaxe: {teclado[teclado.index("c")]} e eu posso cortar a string com a função slice conforme mostro a seguir: {teclado.rindex("T")}') 

#Desafio 1
#Encontre o ídice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(f"ìndice de 'o' dentro da variável biblioteca: {biblioteca.index('o')}")

#Desafio 2
#Usando das palavras
texto = 'Desenvolvimento De Aplicações'
frase = texto.split()
#Imprima apenas a palávra 'De Aplicações
print(f'Resultado: {frase[1]} {frase[2]}')