import csv

from postgres_workshop.db import PostgresDb
from postgres_workshop.measure import measure


@measure
def export_copy(logger, csv_path):
    conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
    query = "COPY (SELECT data->>'location' as location, \
data->>'uri' as uri, \
data->>'num_requests' as num_requests, \
data->>'bytes' as bytes, \
data->>'ip' as ip \
FROM events WHERE \
data->>'location'='MAD50' AND \
data->>'num_requests'='1') TO '{}' DELIMITER ',' CSV HEADER".format(csv_path)
    conn.execute(query)
    logger.info('Done writing')


@measure
def export_line_by_line_json(logger, csv_path):
    conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
    query = "SELECT data FROM events WHERE data->>'location'='MAD50' and data->>'num_requests'='1'"
    records = conn.execute(query)

    with open(csv_path, 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['uri', 'ip', 'location', 'num_requests', 'bytes'])
        dict_writer.writeheader()
        for idx, row in enumerate(records):
            dict_writer.writerow(row[0])
            if idx % 1000 == 0:
                print('1000 inserted: {}'.format(idx))
    logger.info('Done writing')


@measure
def export_line_by_line(logger, csv_path):
    conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
    query = "SELECT data->'location' as location, \
data->>'uri' as uri, \
data->>'num_requests' as num_requests, \
data->>'bytes' as bytes, \
data->>'ip' as ip \
FROM events WHERE \
data->>'location'='MAD50' and data->>'num_requests'='1'"
    records = conn.execute(query)

    with open(csv_path, 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['location', 'uri', 'num_requests', 'bytes', 'ip'])
        for idx, row in enumerate(records):
            writer.writerow(row)
            if idx % 1000 == 0:
                print('1000 inserted: {}'.format(idx))
    logger.info('Done writing')
