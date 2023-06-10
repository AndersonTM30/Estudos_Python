# Quando usar módulos
"""
1 - Separar funcionalidades relacionadas
2 - Não acoplar o seu código

"""

from banco_de_dados import buscar_usuario
from configuracoes import obter_senha
from mensagens_padroes import boas_vindas, novo_usuario, falha_cadastro

buscar_usuario()
obter_senha()

print(boas_vindas)
print(novo_usuario)
print(falha_cadastro)
