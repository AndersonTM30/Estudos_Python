# classe
class Computador:
    #variável global
    sistema_operacional = 'Windows 10'
    # método construtor
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    # métodos da classe (aqui é onde são adicionadas funcionalidades na classe)
    def ligar(self):
        print('Ligando o computdor')

Computador.sistema_operacional = 'Windows 7'

computador = Computador('Dell', '8gb', 'NVIDIA')
computador.marca = 'ASUS'
print(f'Computador: {computador.marca} - Sistema Operacional: {computador.sistema_operacional}')

Computador.sistema_operacional = 'Mac'

computador2 = Computador('Asus', '16gb', 'ATI')
computador2.marca = 'Positivo'
print(f'Computador: {computador2.marca} - Sistema Operacional: {computador2.sistema_operacional}')