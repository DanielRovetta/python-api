from Business import PessoaBusiness, ClienteBusiness
from DTO import PessoaDTO, ClienteDTO


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

    def uptade(self, pessoa: dict):
        self.__init__()
        id = self.pessoa_bussines.uptade(pessoa)
        return self.__obterListaObjetoDTO(self.pessoa_bussines.getById(id))

    def delete(self, pessoa: dict):
        self.__init__()
        return self.pessoa_bussines.delete(pessoa)


class ClienteFacades:
    def __init__(self):
        self.cliente_bussines = ClienteBusiness()
        self.pessoa_facade = PessoaFacades()

    def __obterListaObjetoDTO(self, lista: list):
        lista_dto = []

        for item in lista:
            objeto_dto = ClienteDTO(item.id_cliente, item.dt_criacao, item.dt_exclusao,
                                    self.pessoa_facade.getById(item.id_pessoa)[0])
            lista_dto.append(objeto_dto)

        return lista_dto

    def getAll(self):
        self.__init__()
        return self.__obterListaObjetoDTO(self.cliente_bussines.getAll())

    def getById(self, id: int):
        self.__init__()
        return self.__obterListaObjetoDTO(self.cliente_bussines.getById(id))

    def insert(self, cliente: dict):
        self.__init__()
        id = self.cliente_bussines.insert(cliente)
        return self.__obterListaObjetoDTO(self.cliente_bussines.getById(id))

    def uptade(self, cliente: dict):
        self.__init__()
        id = self.cliente_bussines.uptade(cliente)
        return self.__obterListaObjetoDTO(self.cliente_bussines.getById(id))

    def delete(self, cliente: dict):
        self.__init__()
        return self.cliente_bussines.delete(cliente)
