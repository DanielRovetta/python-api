from Business import PessoaBusiness
from DTO import PessoaDTO


class PessoaFacades:
    def __init__(self):
        self.pessoa_bussines = PessoaBusiness()

    @staticmethod
    def __obterListaObjetoDTO(lista: list):
        lista_dto = []

        for item in lista:
            objeto_dto = PessoaDTO(item.id_pessoa, item.nm_pessoa, item.dt_nascimento,
                                   item.cd_cpf, item.tx_sexo, item.nr_altura, item.nr_peso)
            lista_dto.append(objeto_dto)

        return lista_dto

    def getAll(self):
        self.__init__()
        return self.__obterListaObjetoDTO(self.pessoa_bussines.getAll())

    def getById(self, id: int):
        self.__init__()
        return self.__obterListaObjetoDTO(self.pessoa_bussines.getById(id))

    def insert(self, nova_pessoa: dict):
        self.__init__()
        id = self.pessoa_bussines.insert(nova_pessoa)
        return self.__obterListaObjetoDTO(self.pessoa_bussines.getById(id))
