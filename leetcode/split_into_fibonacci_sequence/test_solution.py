import pytest

from leetcode_py import logged_test

from .helpers import assert_split_into_fibonacci, run_split_into_fibonacci
from .solution import Solution


class TestSplitIntoFibonacciSequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            ("1101111", [11, 0, 11, 11]),
            ("112358130", []),
            ("0123", []),
            ("0000", [0, 0, 0, 0]),
            ("123456579", [123, 456, 579]),
            ("112358", [1, 1, 2, 3, 5, 8]),
            ("011235", [0, 1, 1, 2, 3, 5]),
            ("10235", []),
            ("5473", []),
            ("199100199", [1, 99, 100, 199]),
            ("1234", []),
            ("2147483647", []),
            ("10234", []),
            ("987", []),
            ("011222", []),
            ("12345678", []),
            ("132456", []),
            ("175325500825", [175, 325, 500, 825]),
            ("43155486541", [431, 55, 486, 541]),
            ("52428480908", [52, 428, 480, 908]),
            ("48382430812", [48, 382, 430, 812]),
            ("260137397534", [260, 137, 397, 534]),
            ("131238369607", [131, 238, 369, 607]),
            ("105165270435", [105, 165, 270, 435]),
        ],
    )
    def test_split_into_fibonacci(self, num: str, expected: list[int]):
        result = run_split_into_fibonacci(Solution, num)
        assert_split_into_fibonacci(result, expected)
