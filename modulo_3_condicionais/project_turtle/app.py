from turtle import Turtle
# Iniciar uma turtle
t = Turtle()
# # Definir a velocidade
# t.speed(1)
# #Movimenta a turtle para frente
# t.forward(100)
# # Rotaciona em X graus para a direita
# t.right(10)
# t.forward(100)
# # Rotaciona em X graus para a esquerda
# t.left(10)
# t.forward(100)
# # Movimenta a turtle para trás
# t.backward(200)

while True:
    direcao = input('para qual direção deseja ir? f:frente, r:direita, l:esquerda, b:trás, n:encerra o aplicativo -')
    if direcao == 'f':
        pixels = int(input('Quantos pixels deseja andar? '))
        t.forward(pixels)
    elif direcao == 'r':
            pixels = int(input('Quantos pixels deseja girar? '))
            t.right(pixels)
            t.forward(100)
    elif direcao == 'l':
        pixels = int(input('Quantos pixels deseja girar? '))
        t.left(pixels)
        t.forward(100)
    elif direcao == 'b':
        pixels = int(input('Quantos pixels deseja andar? '))
        t.backward(pixels)

    continua = input('Deseja continuar? s:sim, n:não -')
    if continua == 's':
        continue
    else:
        break
