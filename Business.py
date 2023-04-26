from DAO import PessoaDAO
from Modelos import Pessoa


class PessoaBusiness:
    def __init__(self):
        self.pessoa_dao = PessoaDAO()

    def getAll(self):
        lista = []
        dados = self.pessoa_dao.getAll()
        for item in dados:
            objeto = Pessoa(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            lista.append(objeto)
        return lista
