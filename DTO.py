class PessoaDTO:
    def __init__(self, id_pessoa, nm_pessoa, dt_nascimento, cd_cpf, tx_sexo, nr_altura, nr_peso):
        self.id = id_pessoa
        self.nome = nm_pessoa
        self.data_nascimento = dt_nascimento
        self.cpf = cd_cpf
        self.sexo = tx_sexo
        self.altura = nr_altura
        self.peso = nr_peso
