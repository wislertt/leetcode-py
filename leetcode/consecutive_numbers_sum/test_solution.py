import pytest

from leetcode_py import logged_test

from .helpers import assert_consecutive_numbers_sum, run_consecutive_numbers_sum
from .solution import Solution


class TestConsecutiveNumbersSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 1),
            (5, 2),
            (6, 2),
            (8, 1),
            (9, 3),
            (15, 4),
            (16, 1),
            (21, 4),
            (45, 6),
            (100, 3),
            (945, 16),
            (1000, 4),
            (1048576, 1),
            (1000000000, 10),
            (999999937, 2),
            (999999999, 20),
            (511, 4),
            (512, 1),
            (100000000, 9),
        ],
    )
    def test_consecutive_numbers_sum(self, n: int, expected: int):
        result = run_consecutive_numbers_sum(Solution, n)
        assert_consecutive_numbers_sum(result, expected)
