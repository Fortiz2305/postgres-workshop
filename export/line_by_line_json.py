import logging
import csv

from db import PostgresDb
from measure import measure


@measure
def export_with_csv_json(logger):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "SELECT data FROM events WHERE data->>'location'='MAD50' and data->>'num_requests'='1'"
    records = conn.execute(query)

    with open('./test_json.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['uri', 'ip', 'location', 'num_requests', 'bytes'])
        dict_writer.writeheader()
        for row in records:
            dict_writer.writerow(row[0])
    logger.info('Done writing')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    export_with_csv_json(logger)
