from Business import PessoaBusiness
from DTO import PessoaDTO


class PessoaFacades:
    def __init__(self):
        self.pessoa_bussines = PessoaBusiness()

    def getAll(self):
        self.__init__()
        lista = self.pessoa_bussines.getAll()
        lista_dto = []

        for item in lista:
            objeto_dto = PessoaDTO(item.id_pessoa, item.nm_pessoa, item.dt_nascimento,
                                   item.cd_cpf, item.tx_sexo, item.nr_altura, item.nr_peso)
            lista_dto.append(objeto_dto)

        return lista_dto
