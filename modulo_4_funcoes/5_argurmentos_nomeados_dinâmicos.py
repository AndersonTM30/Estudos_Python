"""
Para funções com argumentos nomeados dinâmicos utiliza-se dois asteríscos (**) no início da função
"""

def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Anderson', 3, 4,5, 6,7, a=1, b=3)