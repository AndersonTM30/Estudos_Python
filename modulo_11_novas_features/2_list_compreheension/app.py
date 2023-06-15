
# Criando um list compreheension com números
nova_lista = [2 * i for i in range(10)]
print(nova_lista)

nomes = ['Anderson', 'Antero', 'Alisson', 'Marcyo', 'Matheus']

# gerando lista de strings
print([nome + ' Aprovado' for nome in nomes])

def adicionar_nome(nome):
    return nome + ' Alterado'

print([adicionar_nome(nome) for nome in nomes]) # gerando lista com funções

from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)]) # gerando uma matriz

# gerando uma lista com função e condicional
print([adicionar_nome(nome) for nome in nomes if nome != 'Matheus'])

# valores numéricos
print([i for i in range(20) if i not in (1, 5, 15, 19)])

def numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
    
print([i for i in range(20) if numero_par(i)])

# if flexível na lista
participantes = ['Larissa', 'Rafael', 'Marcus', 'Jhon']
ganhadores = ['Marcus', 'Jhon']
print([i + ' Ganhador' if i in ganhadores else i + ' Não Selecionado' for i in participantes])

print('==================== Desafio ==================')
print([i for i in range(1, 11) if numero_par(i)])

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']

print([str(indice) + ' - ' + cor for indice, cor in enumerate(cores, 1)])

participantes = ['joel', 'jessica', 'maria', 'cris', 'larissa', 'rafael', 'marcus', 'john']
pagamento_realizado = ['joel', 'jessica', 'maria', 'cris']

print([i + ' Pago' if i in pagamento_realizado else i for i in participantes])