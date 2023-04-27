class Pessoa:

    id_pessoaa: int
    nm_pessoa: str
    dt_nascimento: str
    cd_cpf: str
    tx_sexo: str
    nr_altura: float
    nr_peso: float

    def __init__(self, id_pessoa: int, nm_pessoa: str, dt_nascimento: str, cd_cpf:
                 str, tx_sexo: str, nr_altura: float, nr_peso: float):
        self.id_pessoa = id_pessoa
        self.nm_pessoa = nm_pessoa
        self.dt_nascimento = dt_nascimento
        self.cd_cpf = cd_cpf
        self.tx_sexo = tx_sexo
        self.nr_altura = nr_altura
        self.nr_peso = nr_peso

