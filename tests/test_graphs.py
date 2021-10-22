# -*- coding: utf-8 -*-
import pytest

from xgen.graphs import codec, Bitmap


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [4]),
        ([0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 3]),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10]),
        ([0, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1]),
        ([1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2, 1]),
        ([0, 1, 0, 0, 1, 1, 0, 0, 1, 0], [1, 2, 1]),
        ([0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [1, 1]),
        ([0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [8]),
    ],
)
def test_codec(nums, expected):
    actual = codec(nums)
    assert actual == expected


@pytest.mark.parametrize(
    'matrix, expected',
    [
        ([
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ],
            {
            "rows": [
                [4], [1, 3], [10], [1, 1, 1, 1],
                [1, 2, 1], [1, 2, 1], [1, 1, 1, 1],
                [1, 2, 1], [1, 1], [8]],
            "columns": [
                [1, 2], [2, 2, 1], [2, 2], [1, 2, 1, 1],
                [1, 1, 2, 1, 1], [3, 2, 1, 1], [4, 1, 1],
                [2, 2], [2, 2, 1], [1, 2]]
        }),
    ],
)
def test_dna(matrix, expected):
    bitmap = Bitmap(matrix)
    actual = bitmap.dna()
    assert len(actual) == len(expected)
    assert actual['rows'] == expected['rows']
    assert actual['columns'] == expected['columns']
