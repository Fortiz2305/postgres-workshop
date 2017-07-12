import click
from util.log import get_logger
from misc import clean_db, count

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


if __name__ == '__main__':
    cli()
