from postgres_workshop.db import PostgresDb


def count(logger):
    conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
    query = "select count(*) from trips"
    count = conn.execute(query)
    logger.info("total records: {}".format(count[0][0]))


def clean_db(logger):
    logger.info("Cleaning database")
    conn = PostgresDb('workshop', 'postgres', 'db', 'postgres')
    query = "delete from trips"
    conn.execute(query)
    logger.info("Finished")
