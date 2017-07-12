import pep8
import os

# Just add here the local path of the excluded file (example: 'test/unit/test_to_ignore.py')
EXCLUDED_FILES = ['scripts', 'resources']

# Add the local directories you wish to lint (example: 'src', 'config, 'test', etc)
CHECKED_DIRS = ['postgres_workshop', 'tests']


def root_path():
    this_path = os.path.normpath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(this_path, os.pardir, os.pardir))


def get_excluded_files():
    result = []
    for path in EXCLUDED_FILES:
        result.append(os.path.join(root_path(), path))
    return result


def test_pep8():
    pep8style = pep8.StyleGuide(config_file='linter.cfg', exclude=get_excluded_files())
    result = pep8style.check_files(CHECKED_DIRS)
    assert result.total_errors == 0
