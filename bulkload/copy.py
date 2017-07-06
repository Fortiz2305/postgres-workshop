import logging

from db import PostgresDb
from measure import measure


@measure
def copy_from(logger, file_):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "COPY events2(id, ts, category, type, user_id, data) \
FROM '{}' DELIMITER ',' CSV HEADER".format(file_)
    conn.execute(query)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    copy_from(logger, '../resources/sample-500k.csv')
