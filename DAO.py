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

    def update(self, valores: tuple):
        self.con.__int__()
        self.con.executaQuery("update clinica.pessoa set nm_pessoa = %s, dt_nascimento = %s , cd_cpf = %s, "
                              "tx_sexo = %s, nr_altura = %s, nr_peso = %s where id_pessoa = %s;", valores)

        return valores[-1]

    def delete(self, id: int):
        self.con.__int__()
        self.con.executaQuery("delete from clinica.pessoa where id_pessoa = " + str(id) + ";", id)
        return True


class ClienteDAO:
    def __init__(self):
        self.con = ConexaoPostgres()

    def getAll(self):
        self.con.__int__()
        return self.con.consultaQuery("select id_cliente, dt_criacao, dt_exclusao, id_pessoa "
                                      "from clinica.cliente;")

    def getById(self, id: int):
        self.con.__int__()
        return self.con.consultaQuery("select id_cliente, dt_criacao, dt_exclusao, id_pessoa "
                                      "from clinica.cliente where id_cliente = " + str(id) + ";")

    def insert(self, valores: tuple):
        self.con.__int__()
        self.con.executaQuery("insert into clinica.cliente (dt_criacao, dt_exclusao, id_pessoa) "
                              "values (%s, %s, %s)", valores)

        return self.con.consultaQuery("select MAX(id_pessoa) from clinica.cliente;")

    def update(self, valores: tuple):
        self.con.__int__()
        self.con.executaQuery("update clinica.cliente set dt_criacao = %s, dt_exclusao = %s , id_pessoa = %s "
                              "where id_cliente = %s;", valores)

        return valores[-1]

    def delete(self, id: int):
        self.con.__int__()
        self.con.executaQuery("delete from clinica.cliente where id_cliente = " + str(id) + ";", id)
        return True
