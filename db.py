import psycopg2
from psycopg2.extras import execute_values


class PostgresDb:

    def __init__(self, name, user, host='localhost', password=None):
        self.name = name
        self.user = user
        self.host = host
        self.password = password
        self.connection = None
        self.connected = False

    def execute(self, db_query, params=None, disconnect=True):
        if not self.connected:
            self._connect()
        result = None
        try:
            result = self._run(db_query, params)
        except psycopg2.Error as e:
            raise
        finally:
            if disconnect:
                self.disconnect()
        return result

    def execute_values(self, db_query, params=None, page_size=100, disconnect=True):
        if not self.connected:
            self._connect()
        result = None
        if not params:
            params = ()
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    execute_values(cursor, db_query, params, page_size=page_size)
                    if db_query.strip().upper().startswith('SELECT'):
                        result = cursor.fetchall()
                    else:
                        result = True
        except psycopg2.Error as e:
            raise
        finally:
            if disconnect:
                self.disconnect()
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

    def disconnect(self):
        self.connection.close()
        self.connected = False
