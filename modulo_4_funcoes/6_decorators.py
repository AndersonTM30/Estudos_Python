def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns!!!')

parabenizar()

# Desafio - Crie um decorador que irá pegar a função que for passado para ele e imprimir o horário atual antes de executar a função e depios imprimir o horário após ter finalizado a execução da função.
    # Dica: Você terá que usar o módulo datetime para conseguir o horário atual

from datetime import datetime

def hora_atual(funcao):
    def wrapper():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return wrapper

@hora_atual
def compra():
    print('Comprou uma Viagem sem volta')

compra()