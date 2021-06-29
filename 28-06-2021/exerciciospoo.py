# 1.a) Crie uma classe pessoa com os seguintes atributos: nome,
#sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de
#uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e
#métodos.


class Pessoa:

    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade




    def dados(self):
        print('nome completo:', self.nome, self.sobrenome)
        print('idade: ', self.idade)


individuo = Pessoa('Vinicius', 'Florencio', 25)
print(individuo.nome)
print(individuo.sobrenome)
print(individuo.idade)
individuo.dados()

