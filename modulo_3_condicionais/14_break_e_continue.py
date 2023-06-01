# continue pula ou ignora a linha atual
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         continue


# break interrompe o loop
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         break

# frutas = ['banana', 'maça', 'pera', 'uva']
# for fruta in frutas:
#     if fruta == 'banana':
#         continue
#     print(fruta)

# Desafio - Ao chegar ao estilo "Rap" o mesmo não dev ser impresso na tela.
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

# Desafio 2 - Ao chegar ao estilo "Rock" a execução deve ser interrompida
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
        print(estilo)
