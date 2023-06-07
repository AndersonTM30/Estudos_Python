import logging

logging.basicConfig(
    level=logging.DEBUG
    , filename='modulo_6_tratamento_de_erros/error.log'
    , filemode='a'
    , format='%(asctime)s - [%(levelname)s] - %(message)s - (%(filename)s:%(lineno)d - %(funcName)s)'
    , datefmt='%d/%m/%Y %H:%M:%S'
)

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha bancária: '))
    if senha == '1234':
        print('Cadastro realizado com sucesso!')
except ValueError as error:
    print(f'Por favor digitar apenas números')
    logging.warning(error)

