import config

from db import DB


def run(*args, **kw):
    db = DB(name=config.DB_NAME, user=config.DB_USER)
    db.execute("""SELECT * from actor""")


if __name__ == '__main__':
    run()
