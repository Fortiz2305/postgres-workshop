import logging

from db import PostgresDb
from measure import measure


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
    export_with_copy(logger)
