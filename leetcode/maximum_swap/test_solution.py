import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_swap, run_maximum_swap
from .solution import Solution


class TestMaximumSwap:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (2736, 7236),
            (9973, 9973),
            (0, 0),
            (1, 1),
            (9, 9),
            (10, 10),
            (11, 11),
            (98, 98),
            (1993, 9913),
            (9931, 9931),
            (120, 210),
            (909, 990),
            (10000000, 10000000),
            (987654321, 987654321),
            (100000000, 100000000),
            (999999999, 999999999),
            (2736736, 7736236),
            (98368, 98863),
        ],
    )
    def test_maximum_swap(self, num: int, expected: int):
        result = run_maximum_swap(Solution, num)
        assert_maximum_swap(result, expected)
