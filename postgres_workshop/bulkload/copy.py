from postgres_workshop.db import PostgresDb
from postgres_workshop.measure import measure
from postgres_workshop.util.log import get_logger


@measure
def copy_from(logger, file_):
    conn = PostgresDb(name='copy_test', user='postgres')
    query = "COPY events2(id, ts, category, type, user_id, data) \
FROM '{}' DELIMITER ',' CSV HEADER".format(file_)
    conn.execute(query)


if __name__ == '__main__':
    logger = get_logger(__name__)
    copy_from(logger, '../resources/sample-500k.csv')
