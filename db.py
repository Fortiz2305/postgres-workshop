import psycopg2


class PostgresDb:

    def __init__(self, name, user, host='localhost', password=None):
        self.name = name
        self.user = user
        self.host = host
        self.password = password
        self.connection = None
        self.connected = False

    def execute(self, db_query, params=None):
        if not self.connected:
            self._connect()
        result = None
        try:
            result = self._run(db_query, params)
        except psycopg2.Error as e:
            raise
        finally:
            self._disconnect()
        return result

    def _run(self, query, params=None):
        if not params:
            params = ()
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if query.strip().upper().startswith('SELECT'):
                    query_result = cursor.fetchall()
                else:
                    query_result = True

            return query_result

    def _connect(self):
        if not self.connection or self.connection.closed:
            self.connection = psycopg2.connect(dbname=self.name,
                                               user=self.user,
                                               host=self.host,
                                               password=self.password)

    def _disconnect(self):
        self.connection.close()
        self.connected = False
