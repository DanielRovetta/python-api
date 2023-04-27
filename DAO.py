from Conexao import ConexaoPostgres


class PessoaDAO:
    def __init__(self):
        self.con = ConexaoPostgres()

    def getAll(self):
        self.con.__int__()
        return self.con.consultaQuery("SELECT id_pessoa, nm_pessoa, dt_nascimento, "
                                      "cd_cpf, tx_sexo, nr_altura, nr_peso FROM clinica.pessoa;")

    def getById(self, id: int):
        self.con.__int__()
        return self.con.consultaQuery("select id_pessoa, nm_pessoa, dt_nascimento, cd_cpf, tx_sexo, "
                                      "nr_altura, nr_peso from clinica.pessoa where id_pessoa = " + str(id) + ";")

    def insert(self, valores: tuple):
        self.con.__int__()
        self.con.executaQuery("insert into clinica.pessoa (nm_pessoa, dt_nascimento, cd_cpf, tx_sexo,"
                              "nr_altura, nr_peso) values (%s, %s, %s, %s, %s, %s)", valores)

        return self.con.consultaQuery("select MAX(id_pessoa) from clinica.pessoa;")

