class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá, sou uma pessoa, vamos ao evento?')


class Profissional:
    nome = 'Sou um profissional'

    def convidar(self):
        print('Olá, sou um profissional, vamos ao evento?')

class AtorProfissional(Pessoa, Profissional):
    pass

# Para saber qual propriedade será usada primeiro caso a herança múltipla tiverem as mesma propriedades, usa-se a função mro(Method Resolution Order)
print(AtorProfissional.mro())
ator_profissional = AtorProfissional()
