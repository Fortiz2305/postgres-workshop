import csv

from db import PostgresDb
from measure import measure
from util.log import get_logger


@measure
def export_with_csv_json(logger):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "SELECT data FROM events WHERE data->>'location'='MAD50' and data->>'num_requests'='1'"
    records = conn.execute(query)

    with open('./test_json.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['uri', 'ip', 'location', 'num_requests', 'bytes'])
        dict_writer.writeheader()
        for idx, row in enumerate(records):
            dict_writer.writerow(row[0])
            if idx % 1000 == 0:
                print('1000 inserted: {}'.format(idx))
    logger.info('Done writing')


if __name__ == '__main__':
    logger = get_logger(__name__)
    export_with_csv_json(logger)
