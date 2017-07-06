import logging
import csv
import argparse

from db import PostgresDb
from measure import measure


@measure
def export_with_csv(logger):
    conn = PostgresDb(name='postgres', user='postgres')
    query = "SELECT * FROM events"
    records = conn.execute(query)

    with open('./test1.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['uri', 'ip', 'location', 'num_requests', 'bytes'])
        for row in records:
            writer.writerow(row)
    logger.info('Done writing')


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


@measure
def export_with_copy(logger):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "COPY (SELECT data->>'location' as location, \
data->>'uri' as uri, \
data->>'num_requests' as num_requests, \
data->>'bytes' as bytes, \
data->>'ip' as ip \
FROM events WHERE \
data->>'location'='MAD50' AND \
data->>'num_requests'='1') TO '/home/fortiz/Developments/postgres-workshop/test.csv' DELIMITER ',' CSV HEADER"
    conn.execute(query)
    logger.info('Done writing')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='export_to_file_cli')
    parser.add_argument('--format', required=True, help='Format to use: copy or csv_module')

    args = parser.parse_args()

    if args.format == 'copy':
        export_with_copy(logger)
    elif args.format == 'csv_module':
        export_with_csv(logger)
    elif args.format == 'csv_json':
        export_with_csv_json(logger)
    else:
        print('Invalid format: You have to use copy, csv_module or csv_json')
