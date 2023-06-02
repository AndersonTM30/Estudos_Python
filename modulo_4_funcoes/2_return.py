# Processasr VS Retornar
# Função que apenas processa dados
def cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

cotacao_do_dia('usd')

# funções que retornam dados
def cotacao_do_dia2(moeda):
    if moeda == 'usd':
        return 5.47
    
contacao = cotacao_do_dia2('usd')

if(contacao < 5):
    print('Investir na bolsa americana')
else:
    print('Não investir')

"""
Como escolher entre função que processam ou que retornam dados?
    Eu vou precisar de usar essa informação na lógica do meu programa ainda? 
        Crie uma função que retorne os dados
    Eu só preciso processar esse dados, mas não irei utilizar mais ele depois?
        Crie uma função que apenas processe os dados
"""