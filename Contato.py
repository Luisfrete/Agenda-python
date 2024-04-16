class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def __saudacao__(self):
        print(f"{self.nome}, {self.telefone}")

person = Contato(input("Digite o seu nome:"), input("Digite o seu telefone: "))

print(person)
person.__saudacao__()