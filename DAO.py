from Conexao import ConexaoPostgres


class PessoaDAO:
    def __init__(self):
        self.con = ConexaoPostgres()

    def getAll(self):
        self.con.__int__()
        return self.con.consultaQuery("select * from clinica.pessoa p;")
