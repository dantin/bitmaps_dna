# -*- coding: utf-8 -*-
import json
import logging
from typing import List

from xgen.graphs import Bitmap


logger = logging.getLogger(__name__)


def load_bitmap(filename) -> List[Bitmap]:
    rets = []
    with open(filename) as f:
        for bits in json.load(f):
            rets.append(Bitmap(bits))
    return rets


def cli(filename: str):
    bitmaps = load_bitmap(filename)
    logger.debug('bitmap size %d', len(bitmaps))
    # for i, m in enumerate(bitmaps):
    #     print(i, m)
    print(bitmaps[0].dna())
