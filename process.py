import logging
import sys


def exit_if_false(condition):
    if not condition:
        logging.error('terminating process...')
        sys.exit(1)
