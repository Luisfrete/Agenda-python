
class Verificar:
    def __init__(self):
        self.agenda = None
        self.nome = None

    def verContatos(self, nome):

        for contato in  self.agenda.contatos:
            if contato.nome == nome:
                print(f"Contato {nome} encontrado na agenda.")
                return nome
            else:
                print(f"Contato {nome} não encontrado na agenda.")
 
           


if __name__ == "__main__" :
    from Adicionar import Adicionar
    nome = None("", "")
    nome.__toString__()



        