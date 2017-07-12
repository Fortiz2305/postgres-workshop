import click
from postgres_workshop.util.log import get_logger
from postgres_workshop.misc import clean_db, count
from postgres_workshop.bulkload.insert_flavours import (
    insert_line_by_line,
    insert_line_by_line_prepared_statements,
    batch_insert,
    insert_copy
)

logger = get_logger(__name__)


@click.group()
def cli():
    pass


@cli.command()
def cleandb():
    clean_db(logger)


@cli.command()
def records_count():
    count(logger)


@cli.command()
@click.option('--mode', type=click.Choice(['line-by-line', 'prep-stat', 'batch', 'copy']),
              default='line-by-line')
def insert(mode):
    modes = {
        'line-by-line': insert_line_by_line,
        'prep-stat': insert_line_by_line_prepared_statements,
        'batch': batch_insert

    }
    if mode == 'copy':
        insert_copy(logger)
    else:
        modes[mode](logger=logger, csv_path='./resources/2015-Q2-Trips-History-Data.csv')


if __name__ == '__main__':
    cli()
