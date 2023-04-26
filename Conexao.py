import psycopg2


class ConexaoPostgres:
    def __int__(self, host="localhost", database="postgres", user="postgres", password="itix.123"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __conectarPostgres(self):
        try:
            return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        except (Exception, psycopg2.DatabaseError) as error:
            raise error

    def executaQuery(self, query):
        con = self.__conectarPostgres()
        cur = con.cursor()

        try:
            cur.execute(query)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            con.rollback()
            raise error

        cur.close()
        con.close()

    def consultaQuery(self, query):
        con = self.__conectarPostgres()
        cur = con.cursor()
        try:
            cur.execute(query)
            recset = cur.fetchall()
            registros = []
            for rec in recset:
                registros.append(rec)

        except (Exception, psycopg2.DatabaseError) as error:
            raise error

        cur.close()
        con.close()
        return registros


class ConexaoMysql:
    pass
