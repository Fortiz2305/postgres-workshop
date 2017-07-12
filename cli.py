import click
from util.log import get_logger
from misc import clean_db, count
from bulkload.insert_flavours import (
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
        'batch': batch_insert,
        'copy': insert_copy

    }
    modes[mode](logger)


if __name__ == '__main__':
    cli()
