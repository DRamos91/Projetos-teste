class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrar_nome(self):
        print(self.nome)
    def mostrar_idade(self):
        print(self.idade)

class Estudante(Pessoa):
    def __init__ (self, nome, idade, mat):
        Pessoa.__init__ (self, nome, idade)
        self.mat = mat
    def mostrar_mat(self):
        print(self.mat)

p = Pessoa ("DANIEL", 30)
p.mostrar_idade()