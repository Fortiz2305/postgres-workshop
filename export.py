import logging
import csv
import argparse

from db import PostgresDb
from measure import measure


@measure
def export_with_csv(logger):
    conn = PostgresDb(name='workshop', user='postgres')
    query = "SELECT * FROM trips"
    records = conn.execute(query)

    with open('./test1.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['duration_ms', 'start_time', 'start_terminal', 'end_time', 'end_terminal',
                         'bike_number', 'subscription_type'])
        for row in records:
            writer.writerow(row)
    logger.info('Done writing')


@measure
def export_with_copy(logger):
    conn = PostgresDb(name='workshop', user='postgres')
    query = "COPY (SELECT * FROM trips) TO '/Users/Fortiz/Developments/postgres-workshop/test.csv' DELIMITER ';' CSV HEADER"
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
    else:
        print('Invalid format: You have to use copy or csv_module')
