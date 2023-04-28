import psycopg2
from ExecutionException import ErroBancoDeDados
from ExecutionException import ErroExecutarConsulta


class ConexaoPostgres:
    def __int__(self, host="localhost", database="postgres", user="postgres", password="itix.123"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __conectarPostgres(self):
        try:
            return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        except (Exception, psycopg2.DatabaseError, psycopg2.OperationalError) as error:
            raise ErroBancoDeDados("Erro ao conectar ao Banco de Dados: " + str(error))

    def executaQuery(self, query, valores):
        con = self.__conectarPostgres()
        cur = con.cursor()

        try:
            if type(valores) == tuple:
                cur.execute(query, valores)
            else:
                cur.execute(query)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            con.rollback()
            raise ErroExecutarConsulta("Erro ao executar consulta no Banco de Dados: " + str(error))

        finally:
            cur.close()
            con.close()

    def consultaQuery(self, query):
        try:
            con = self.__conectarPostgres()
            cur = con.cursor()
            cur.execute(query)
            dataset = cur.fetchall()
            registros = []

            for data in dataset:
                registros.append(data)

            cur.close()
            con.close()

            return registros

        except (Exception, psycopg2.DatabaseError) as error:
            raise ErroExecutarConsulta("Erro ao executar consulta no Banco de Dados: " + str(error))


class ConexaoMysql:
    pass
