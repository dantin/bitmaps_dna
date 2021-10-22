# -*- coding: utf-8 -*-
from typing import Dict, List


class Bitmap():

    def __init__(self, bits: List[List[int]]):
        self.row_size = len(bits)
        self.col_size = len(bits[0])
        self.bits = bits

    def dna(self) -> Dict[str, List[List[int]]]:
        rows = [codec(row) for row in self.bits]
        cols = []
        for i in range(self.col_size):
            col = [self.bits[j][i] for j in range(self.row_size)]
            cols.append(codec(col))
        return {'rows': rows, 'columns': cols}

    def __str__(self):
        return f'bitmap: ({self.row_size}, {self.col_size})'


def codec(nums: List[int]) -> List[int]:
    """codec returns a one-dimension bit array to int array."""
    low, high = 0, 0
    i = 0
    ret = []
    while i < len(nums):
        low = i
        while low < len(nums):
            if nums[low] == 1:
                break
            low += 1
        high = low
        while high < len(nums):
            if nums[high] == 0:
                break
            high += 1
        if high - low != 0:
            ret.append(high - low)
        i = high
    return ret
