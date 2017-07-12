import csv

from db import PostgresDb
from measure import measure
from util.log import get_logger


@measure
def export_with_csv(logger):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "SELECT data->'location' as location, \
data->>'uri' as uri, \
data->>'num_requests' as num_requests, \
data->>'bytes' as bytes, \
data->>'ip' as ip \
FROM events WHERE \
data->>'location'='MAD50' and data->>'num_requests'='1'"
    records = conn.execute(query)

    with open('./test1.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['location', 'uri', 'num_requests', 'bytes', 'ip'])
        for idx, row in enumerate(records):
            writer.writerow(row)
            if idx % 1000 == 0:
                print('1000 inserted: {}'.format(idx))
    logger.info('Done writing')


if __name__ == '__main__':
    logger = get_logger(__name__)
    export_with_csv(logger)
