import csv
import logging
from db import PostgresDb
from measure import measure
from bulkload import PAGE_SIZE

@measure
def insert_line_by_line(logger):
    with open('../resources/2015-Q2-Trips-History-Data.csv') as trips_csv:
        reader = csv.reader(trips_csv)
        # ignore header
        next(reader)
        conn = PostgresDb('workshop', 'postgres','db', 'postgres')
        for idx, row in  enumerate(reader):
            query = "INSERT INTO trips VALUES(%s, %s, %s, %s, %s, %s, %s)"
            conn.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            if idx % PAGE_SIZE == 0:
                logger.info("{} registros insertados".format(PAGE_SIZE))
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    insert_line_by_line(logger)
