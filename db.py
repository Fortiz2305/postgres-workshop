import psycopg2

from measure import measure


class DB(object):

    def __init__(self, name, user, host='localhost', password=None):
        self.name = name
        self.user = user
        self.host = host
        self.password = password
        self.connection = None
        self.connected = False

    @measure
    def execute(self, db_query):
        if not self.connected:
            self._connect()
        result = None
        try:
            result = self._run(db_query)
        except psycopg2.Error as e:
            raise
        finally:
            self._disconnect()
        return result

    def _run(self, query):
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                if query.strip().upper().startswith('SELECT'):
                    query_result = cursor.fetchall()
                else:
                    query_result = True

            return query_result

    def _connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(dbname=self.name,
                                               user=self.user,
                                               host=self.host,
                                               password=self.password)

    def _disconnect(self):
        self.connected = False
        self.connection.close()
