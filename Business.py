from DAO import PessoaDAO
from Entidades import Pessoa
from BusinessException import DadosNaoEncotrados
from BusinessException import DadosNaoInseridos


class PessoaBusiness:
    def __init__(self):
        self.pessoa_dao = PessoaDAO()

    @staticmethod
    def __obterListaObjetoEntidade(dados: list):
        lista = []
        for item in dados:
            objeto = Pessoa(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            lista.append(objeto)
        return lista

    @staticmethod
    def __validarPessoa(nova_pessoa: dict):
        pessoa = Pessoa(nova_pessoa['id'], nova_pessoa['nome'], nova_pessoa['data_nascimento'], nova_pessoa['cpf'],
                        nova_pessoa['sexo'], nova_pessoa['altura'], nova_pessoa['peso'])

        if pessoa.nm_pessoa is None or len(pessoa.nm_pessoa) == 0 or type(pessoa.nm_pessoa) != str:
            raise DadosNaoEncotrados("Nome inválido")

        if pessoa.nr_peso is None or pessoa.nr_peso == 0 or type(pessoa.nr_peso) != float:
            raise DadosNaoEncotrados("Peso inválido")

        if pessoa.nr_altura is None or pessoa.nr_altura == 0 or type(pessoa.nr_altura) != float:
            raise DadosNaoEncotrados("Altura inválida")

        if pessoa.cd_cpf is None or len(pessoa.cd_cpf) == 0 or type(pessoa.cd_cpf) != str:
            raise DadosNaoEncotrados("CPF inválido")

        if pessoa.tx_sexo is None or len(pessoa.tx_sexo) == 0 or type(pessoa.tx_sexo) != str:
            raise DadosNaoEncotrados("Sexo inválido")

        if pessoa.dt_nascimento is None or len(pessoa.dt_nascimento) == 0 or type(pessoa.dt_nascimento) != str:
            raise DadosNaoEncotrados("Data de Nacimento inválida")

        return pessoa

    def getAll(self):
        lista = self.pessoa_dao.getAll()
        if len(lista) == 0:
            raise DadosNaoEncotrados("Não foram encotrados dados")

        return self.__obterListaObjetoEntidade(lista)

    def getById(self, id: int):
        if id is None or id <= 0 or type(id) != int:
            raise DadosNaoEncotrados("Id informado invalido")

        lista = self.pessoa_dao.getById(id)

        if len(lista) == 0:
            raise DadosNaoEncotrados("Não foram encotrados dados")

        return self.__obterListaObjetoEntidade(lista)

    def insert(self, nova_pessoa: dict):

        pessoa = self.__validarPessoa(nova_pessoa)

        if pessoa is None:
            raise DadosNaoEncotrados("Dados informados são invalidos")

        valores = (pessoa.nm_pessoa, pessoa.dt_nascimento, pessoa.cd_cpf, pessoa.tx_sexo,
                   pessoa.nr_altura, pessoa.nr_peso)

        id = self.pessoa_dao.insert(valores)

        if id == 0 or id is None:
            raise DadosNaoInseridos("Dados não foram iseridos com sucesso")

        return id[0][0]
