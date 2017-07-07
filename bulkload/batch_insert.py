import csv
import logging
from db import PostgresDb
from measure import measure
from bulkload import PAGE_SIZE

# http://initd.org/psycopg/docs/extras.html#fast-exec

@measure
def insert_line_by_line_prepared_statements(logger):
    with open('../resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
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

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    insert_line_by_line_prepared_statements(logger)
