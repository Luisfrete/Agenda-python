class Adicionar:
    def __init__(self, nome, telefone):
        self.name = nome
        self.telefone = telefone

    def __toString__(self):
        print( f"{self.name} {self.telefone}" )
