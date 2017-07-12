import csv
from db import PostgresDb
from measure import measure
from bulkload import PAGE_SIZE


@measure
def insert_line_by_line(logger):
    with open('./resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
        reader = csv.reader(trips_csv)
        # ignore header
        next(reader)
        conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
        for idx, row in enumerate(reader):
            query = "INSERT INTO trips VALUES(%s, %s, %s, %s, %s, %s, %s)"
            conn.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            if idx % PAGE_SIZE == 0:
                logger.info("{} registros insertados".format(PAGE_SIZE))


@measure
def insert_line_by_line_prepared_statements(logger):
    # http://initd.org/psycopg/articles/2012/10/01/prepared-statements-psycopg/
    # https://www.postgresql.org/docs/current/static/sql-prepare.html
    with open('./resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
        reader = csv.reader(trips_csv)
        # ignore header
        next(reader)
        try:
            conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
            prepared_statement = "PREPARE bulkplan as INSERT INTO trips VALUES \
            ($1, $2, $3, $4, $5, $6, $7)"
            conn.execute(prepared_statement, disconnect=False)
            for idx, row in enumerate(reader):
                conn.execute("execute bulkplan (%s, %s, %s, %s, %s, %s, %s)", (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]),
                    disconnect=False)
                if idx % PAGE_SIZE == 0:
                    logger.info("{} registros insertados".format(PAGE_SIZE))
        finally:
            logger.info('closing connection ...')
            conn.disconnect()


@measure
def batch_insert(logger):
    # http://initd.org/psycopg/docs/extras.html#fast-exec
    with open('./resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
        reader = csv.reader(trips_csv)
        # ignore header
        next(reader)
        try:
            conn = PostgresDb('workshop', 'postgres','db', 'postgres')
            # prepared_statement = "PREPARE bulkplan as INSERT INTO trips VALUES ($1, $2, $3, $4, $5, $6, $7)"
            # conn.execute(prepared_statement, disconnect=False)
            arg_list = []
            for idx, row in  enumerate(reader):
                arg_list.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                if idx % PAGE_SIZE == 0:
                    # conn.execute_values("execute bulkplan %s", arg_list, disconnect=False)
                    conn.execute_values("INSERT INTO trips VALUES %s", arg_list, page_size=1000, disconnect=False)
                    logger.info("{} registros insertados".format(PAGE_SIZE))
                    arg_list = []
            else:
                if arg_list:
                    conn.execute_values("execute bulkplan %s", arg_list,
                    page_size=10, disconnect=False)
        finally:
            logger.info('closing connection ...')
            conn.disconnect()


@measure
def insert_copy(logger):
    conn = PostgresDb('workshop', 'postgres','db', 'postgres')
    query = "COPY trips FROM '{}' WITH (FORMAT CSV, HEADER true)".format('/opt/data.csv')
    logger.info('Empezando el COPY')
    conn.execute(query)
    logger.info('COPY finalizado')
