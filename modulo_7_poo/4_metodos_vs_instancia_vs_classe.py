# classe
class Computador:
    #variável global
    sistema_operacional = 'Windows 10'
    # método construtor
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    # Métodos comuns
    def exibir_dados_do_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria_ram} de ram e placa de vídeo {self.placa_de_video} e sistema operacional {self.sistema_operacional}')
    # Métodos de classe
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Baixo Custo')
    
    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Alto Nível')
    # Métodos estáticos
    @staticmethod
    def roda_programas_pesados(memoria_ram: int):
        if memoria_ram >= 8:
            return True
        else:
            return False

computador1 = Computador.computador_escritorio('8gb')
computador2 = Computador.computador_configuracao_pesado('32gb')
computador1.exibir_dados_do_computador()
computador1.roda_programas_pesados(10)
print('===================================')
computador2.exibir_dados_do_computador()