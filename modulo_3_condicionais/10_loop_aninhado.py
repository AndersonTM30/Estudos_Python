paises = ['Brasil', 'Argentina', 'Chile', 'Colombia']
estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']

for pais in paises:
    for estacao in estacoes:
        print(f'{pais} - {estacao}')

for x in range(1, 11):
    for y in range(1, 6):
        print(f'Loop externo {x} - Loop interno {y}')

# Desafio
# Imprima na tela a marca + celular de todos os celulares, usando as informações abaixo:

celulares = ['Asus', 'Samsung', 'Sony', 'Iphone', 'Xiaomi']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'Marca: {celular} - Modelo: {versao}')