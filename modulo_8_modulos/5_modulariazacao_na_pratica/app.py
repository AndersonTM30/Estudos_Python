from banco_de_dados import iniciar_banco_de_dados
from configuracoes import  usuarios_maximos
from processamento_imagem import Camera

iniciar_banco_de_dados()
print(usuarios_maximos)
Camera('720').aumentar_zoom()
