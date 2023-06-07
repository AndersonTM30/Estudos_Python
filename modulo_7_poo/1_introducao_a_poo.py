# classe
class Computador:
    # método construtor
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


computador1 = Computador('Asus', '8gb', 'NVIDIA')
print(f'Computador: {computador1.marca}, com {computador1.memoria_ram} de ram e placa de vídeo {computador1.placa_de_video}')
computador2 = Computador('Dell', '4gb', 'ATI')
print(f'Computador: {computador2.marca}, com {computador2.memoria_ram} de ram e placa de vídeo {computador2.placa_de_video}')