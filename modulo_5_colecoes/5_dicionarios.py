# Dicionários são representados por chave, valor
dicionario_pessoa = {'nome': 'Anderson', 'idade': 31, 'altura': 1.70}
dicionario_pessoa2 = dict(nome='Carol', idade=18, altura=1.60)
print(dicionario_pessoa)
print(dicionario_pessoa2)
# Acessando todas as chaves de um dicionário
print(dicionario_pessoa.keys())
# Acessando um valor dentro de um dicionário
print(dicionario_pessoa['nome'])
print(dicionario_pessoa2['nome'])

# Acessando os valores dentr de um dicionário
print(dicionario_pessoa.values())

# Acessando tanto a chave quanto o valor de um dicionário
print(dicionario_pessoa.items())

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item[1])

"""
Adicionar aluno: O programa deve solicitar o nome do aluno, sua idade e seu número de matrícula. Em seguida,
adicione essas informações a um dicionário, onde a matrícula será a chave e os dados do aluno serão o valor.
"""
lista_alunos = {}


def cadastra_aluno():
    aluno = input('Informe o nome do Aluno: ')
    matricula = input('Informe o número da matrícula do aluno: ')
    lista_alunos[matricula] = {'nome': aluno, 'matricula': matricula}

"""
Consultar aluno: O programa deve solicitar o número de matrícula de um aluno e exibir suas informações (nome e idade) caso ele exista no
sistema. Caso contrário, exiba uma mensagem informando que o aluno não foi encontrado.
"""

def consultar_aluno():
    print('Consultando aluno:')
    matricula = input('Informe a matrícula do aluno: ')
    if matricula in lista_alunos:
        aluno = lista_alunos[matricula]
        print('Informações do aluno: {aluno}')
        print(f'Nome: {aluno["nome"]}\nMatricula: {aluno["matricula"]}')
    else:
        print('Aluno não encontrado!')

"""
Remover aluno: O programa deve solicitar o número de matrícula de um aluno e removê-lo do sistema, caso ele exista. Caso contrário, exiba uma
mensagem informando que o aluno não foi encontrado.
"""

def remover_aluno():
    matricula = input('Informe a matrícula do aluno: ')
    if matricula in lista_alunos:
        del lista_alunos[matricula]
        print('Aluno removido com sucesso!')
    else:
        print('Aluno não encontrado!')


while True:
    cadastra_aluno()
    decisao = input('Deseja continuar cadastrando alunos? ')
    if decisao.lower() not in ('sim', 's'):
        break

consultar_aluno()

remover_aluno()

print(lista_alunos)