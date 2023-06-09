# O conceito de classes abstratas são para cirar contratos (esqueleto) que deve ser implementado na classe que a herda

from abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass


class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando a lente para {tamanho}')


camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(10)

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, claridade):
        pass

    @abstractmethod
    def reduzir_claridade(self, claridade):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, claridade):
        print(f'Aumentando a claridade em {claridade} pontos')

    def reduzir_claridade(self, claridade):
        print(f'Reduzindo a claridade em {claridade} pontos') 


monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)