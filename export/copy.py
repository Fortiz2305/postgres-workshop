from db import PostgresDb
from measure import measure
from util.log import get_logger


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
    logger = get_logger(__name__)
    export_with_copy(logger)
