import pytest

from leetcode_py import logged_test

from .helpers import assert_range_bitwise_and, run_range_bitwise_and
from .solution import Solution


class TestTestBitwiseANDOfNumbersRange:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, left, right, expected",
        [
            (Solution, 5, 7, 4),
            (Solution, 0, 0, 0),
            (Solution, 1, 2147483647, 0),
            (Solution, 1, 1, 1),
            (Solution, 2, 2, 2),
            (Solution, 1, 2, 0),
            (Solution, 4, 7, 4),
            (Solution, 10, 11, 10),
            (Solution, 0, 1, 0),
            (Solution, 7, 15, 0),
            (Solution, 8, 10, 8),
            (Solution, 16, 19, 16),
            (Solution, 6, 7, 6),
            (Solution, 3, 3, 3),
            (Solution, 100, 128, 0),
            (Solution, 2, 3, 2),
            (Solution, 1, 3, 0),
            (Solution, 1073741824, 2147483647, 1073741824),
        ],
    )
    def test_range_bitwise_and(self, solution_class, left: int, right: int, expected: int):
        result = run_range_bitwise_and(solution_class, left, right)
        assert_range_bitwise_and(result, expected)
