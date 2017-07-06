import csv
import logging
from db import PostgresDb
from measure import measure


# http://initd.org/psycopg/articles/2012/10/01/prepared-statements-psycopg/
# https://www.postgresql.org/docs/current/static/sql-prepare.html

@measure
def insert_line_by_line_prepared_statements(logger):
    with open('../resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
        reader = csv.reader(trips_csv)
        # ignore header
        next(reader)
        try:
            conn = PostgresDb('workshop', 'postgres','db', 'postgres')
            prepared_statement = "PREPARE bulkplan as INSERT INTO trips VALUES($1, $2, $3, $4, $5, $6, $7)"
            conn.execute(prepared_statement, disconnect=False)
            for idx, row in  enumerate(reader):
                conn.execute("execute bulkplan (%s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6]), disconnect=False)
                if idx % 1000 == 0:
                    logger.info("1000 registros insertados")
        finally:
            logger.info('closing connection ...')
            conn.disconnect()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    insert_line_by_line_prepared_statements(logger)
