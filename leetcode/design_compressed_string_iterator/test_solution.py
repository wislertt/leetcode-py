import pytest

from leetcode_py import logged_test

from .helpers import assert_string_iterator, run_string_iterator
from .solution import StringIterator


class TestDesignCompressedStringIterator:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "has_next",
                ],
                [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []],
                [None, "L", "e", "e", "t", "C", "o", True, "d", True],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                ],
                [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], [], [], [], []],
                [None, "L", "e", "e", "t", "C", "o", "d", "e", "\x20", "\x20", False, "\x20"],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                ],
                [["a2b2c3"], [], [], [], [], [], [], [], [], [], []],
                [None, "a", "a", "b", "b", True, "c", "c", "c", False, "\x20"],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "has_next",
                ],
                [["a2b2c3"], [], [], [], [], [], [], [], [], [], [], []],
                [None, "a", "a", "b", "b", "c", "c", "c", "\x20", False, "\x20", False],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "has_next",
                ],
                [["x10"], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                [
                    None,
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "x",
                    "\x20",
                    "\x20",
                    False,
                    "\x20",
                    False,
                ],
            ),
            (
                ["StringIterator", "next", "next", "has_next"],
                [["a1"], [], [], []],
                [None, "a", "\x20", False],
            ),
            (
                ["StringIterator", "has_next", "next", "next", "has_next", "has_next"],
                [["a1"], [], [], [], [], []],
                [None, True, "a", "\x20", False, False],
            ),
            (
                ["StringIterator", "next", "next", "has_next", "has_next"],
                [["z1000000000"], [], [], [], []],
                [None, "z", "z", True, True],
            ),
            (
                ["StringIterator", "has_next", "next", "next"],
                [["z1000000000"], [], [], []],
                [None, True, "z", "z"],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "has_next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                ],
                [["X1Y2Z3"], [], [], [], [], [], [], [], [], [], []],
                [None, "X", True, "Y", "Y", True, "Z", "Z", "Z", False, "\x20"],
            ),
            (
                [
                    "StringIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                ],
                [["a9"], [], [], [], [], [], [], [], [], [], []],
                [None, "a", "a", "a", "a", "a", "a", "a", "a", "a", False],
            ),
            (
                ["StringIterator", "next", "next", "has_next", "next", "next", "has_next"],
                [["b3"], [], [], [], [], [], []],
                [None, "b", "b", True, "b", "\x20", False],
            ),
        ],
    )
    def test_string_iterator(
        self, operations: list[str], inputs: list[list[str]], expected: list[str | bool | None]
    ):
        result, _ = run_string_iterator(StringIterator, operations, inputs)
        assert_string_iterator(result, expected)
