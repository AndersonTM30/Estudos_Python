class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a câmera {self.marca} com a qualidade de {self.megapixels} megapixels')

class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com a câmera {self.marca} com a qualidade de {self.megapixels} megapixels, utilizando a câmera #{camera_a_utilizar}')


class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_maxima_de_gravacao):
        super().__init__(marca, megapixels)
        self.horas_maxima_de_gravacao = horas_maxima_de_gravacao

    def rotacionar_camera(self, direcao):
        print(f'Rotacionar a câmera para {direcao}')

# Verifica a classe filha é verdadeira
print(issubclass(CameraCelular, Camera))
print(issubclass(CameraSeguranca, Camera))

camera_celular = CameraCelular('Sony', '25mp', 4)
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto(2)

camera_seguranca = CameraSeguranca('Sony','5mp', 10)
camera_seguranca.rotacionar_camera('Direita')