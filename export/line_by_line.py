import logging
import csv

from db import PostgresDb
from measure import measure


@measure
def export_with_csv(logger):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "SELECT * FROM events"
    records = conn.execute(query)

    with open('./test1.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['uri', 'ip', 'location', 'num_requests', 'bytes'])
        for row in records:
            writer.writerow(row)
    logger.info('Done writing')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    export_with_csv(logger)
