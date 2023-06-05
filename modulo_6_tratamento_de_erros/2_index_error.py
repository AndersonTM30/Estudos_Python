try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(meses[15])
except IndexError as error:
    print('Por favor acessar um índice válido!')
    print(error)