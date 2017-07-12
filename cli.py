#!/usr/bin/env python3

import click
from postgres_workshop.util.log import get_logger
from postgres_workshop.misc import clean_db, count
from postgres_workshop.bulkload.insert_flavours import (
    insert_line_by_line,
    insert_line_by_line_prepared_statements,
    batch_insert,
    insert_copy,
    insert_copy_events
)
from postgres_workshop.export.export_flavours import (
    export_line_by_line,
    export_line_by_line_json,
    export_copy
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
@click.option('--mode', type=click.Choice(['line-by-line', 'prep-stat', 'batch', 'copy', 'copy-events']),
              default='line-by-line')
def insert(mode):
    modes = {
        'line-by-line': insert_line_by_line,
        'prep-stat': insert_line_by_line_prepared_statements,
        'batch': batch_insert,
    }

    if mode == 'copy':
        insert_copy(logger)
    elif mode == 'copy-events':
        insert_copy_events(logger=logger, csv_path='/opt/data_events.csv')
    else:
        modes[mode](logger=logger, csv_path='./resources/2015-Q2-Trips-History-Data.csv')


@cli.command()
@click.option('--mode', type=click.Choice(['line-by-line', 'line-by-line-json', 'copy']),
              default='line-by-line')
def export(mode):
    modes = {
        'line-by-line': export_line_by_line,
        'line-by-line-json': export_line_by_line_json,
    }

    if mode == 'copy':
        export_copy(logger=logger, csv_path='/opt/test.csv')
    else:
        modes[mode](logger=logger, csv_path='./test.csv')


if __name__ == '__main__':
    cli()
