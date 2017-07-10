import csv
from db import PostgresDb
from measure import measure
from util.log import get_logger


@measure
def insert_copy(logger):
    conn = PostgresDb('workshop', 'postgres','db', 'postgres')
    query = "COPY trips FROM '{}' WITH (FORMAT CSV, HEADER true)".format('/opt/data.csv')
    logger.info('Empezando el COPY')
    conn.execute(query)
    logger.info('COPY finalizado')


if __name__ == '__main__':
    logger = get_logger(__name__)
    insert_copy(logger)
