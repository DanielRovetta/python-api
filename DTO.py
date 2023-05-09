class PessoaDTO:
    id: int
    nome: str
    data_nascimento: str
    cpf: str
    sexo: str
    altura: float
    peso: float

    def __init__(self, id: int, nome: str, data_nascimento: str, cpf:
                 str, sexo: str, altura: float, peso: float):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.sexo = sexo
        self.altura = altura
        self.peso = peso


class ClienteDTO:
    id: int
    data_criacao: str
    data_exclusao: str

    pessoa: PessoaDTO

    def __init__(self, id: int, data_criacao: str, data_exclusao: str, pessoa: PessoaDTO):
        self.id = id
        self.data_criacao = data_criacao
        self.data_exclusao = data_exclusao
        self.pessoa = pessoa
