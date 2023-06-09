class Pessoa:
    def __init__(self):
        self.nome = 'Anderson'
        self.habilidades = ['Resolver Problemas', 'Construir aplicativos']

    # Método mágico com a representação para programadores(chamado com o método repr(pessoa))
    def __repr__(self) -> str:
        return 'Classe Pessoa com propriedades nome e habiliades'
    # Método mágico que retorna o que deve ser mensurado para determinar a quantidade daquela classe (chamado com método(len(pessoa)))
    def __len__(self):
        return len(self.habilidades)
    # Método mágico para retornar uma string
    def __str__(self) -> str:
        return f'{self.nome} com as habilidades {self.habilidades}'

pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))# Este método mágico é usado para saber quais outros métodos mágicos podem ser utilizados na classe