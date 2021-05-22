import logging
import sys


def do_nothing():
    pass


def exit_if_false(condition):
    if not condition:
        logging.error('terminating process...')
        sys.exit(1)
