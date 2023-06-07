# classe
class Computador:
    # método construtor
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    # métodos da classe (aqui é onde são adicionadas funcionalidades na classe)
    def ligar(self):
        print('Ligando o computdor')

    def desligar(self):
        print('Desligando o computador')

    def exibir_dados_do_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria_ram} de ram e placa de vídeo {self.placa_de_video}')


computador1 = Computador('Asus', '32gb', 'Nvidia')
computador1.ligar()
computador1.exibir_dados_do_computador()
computador1.desligar()

computador2 = Computador('Dell', '8gb', 'Nvidia')
computador2.ligar()
computador2.exibir_dados_do_computador()
computador2.desligar()