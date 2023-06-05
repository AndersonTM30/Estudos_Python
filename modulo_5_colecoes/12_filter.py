# Filter segue a mesma lógica da função map, porém ele retorna apenas a condição verdadeira do filtro.

nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else: 
        return False

print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))

pinturas = [
    ['Pintura Clássica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))

# Desafio 1 - Usando a lista abaixo, filtre apenas as vagas com salário acima de 2500

vagas = [
    ['vaga 1', 1200],
    ['vaga 1', 2550],
    ['vaga 3', 5000]
]

def consulta_salario_de_vaga(salario):
    if salario[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(consulta_salario_de_vaga, vagas)))