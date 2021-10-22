# -*- coding: utf-8 -*-
import logging
from xgen.cli import cli

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    cli('./bitmap.json')
