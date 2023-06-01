from turtle import Turtle
# Iniciar uma turtle
t = Turtle()
# Definir a velocidade
t.speed(1)

while True:
    distancia = int(input('Distancia a percorrer?'))
    t.forward(distancia)