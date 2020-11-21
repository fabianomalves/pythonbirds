class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=40, ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome e {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mao.'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    fabiano = Mutante(nome='Fabiano')
    luciano = Homem(fabiano, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(fabiano.__dict__)
    print(luciano.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(fabiano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(fabiano.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(fabiano, Pessoa))
    print(isinstance(fabiano, Homem))
    print(fabiano.olhos)
    print(luciano.cumprimentar())
    print(fabiano.cumprimentar())
