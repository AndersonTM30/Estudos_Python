from datetime import datetime

print(datetime.now())

# Criar uma data
data = datetime(2023, 5, 28)
print(data)

# Receber uma data e retorná-la no formato dd/mm/aaaa
data_lancamento = datetime.strptime(input('Quando o aplicativo será lançado? '), '%d/%m/%Y')
print(data_lancamento)
print(type(data_lancamento))

# Calcular prazo entre duas datas
data_atual = datetime.now()

prazo = data_lancamento - data_atual
print(f'Faltam {prazo.days} dias para o lançamento do aplicativo')

# Desafio
# Calcule quantos dias faltam para o seu aniversário
dia_atual = datetime.now()
data_aniversario = datetime.strptime(input('Digite o dia do seu aniversário: '), '%d/%m/%Y')
aniversario = data_aniversario - dia_atual

print(f'Faltam {aniversario.days} dias para o seu aniversário')