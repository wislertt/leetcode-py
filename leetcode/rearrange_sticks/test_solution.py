import pytest

from leetcode_py import logged_test

from .helpers import assert_rearrange_sticks, run_rearrange_sticks
from .solution import Solution


class TestRearrangeSticks:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (3, 2, 3),
            (5, 5, 1),
            (20, 11, 647427950),
            (1, 1, 1),
            (2, 1, 1),
            (2, 2, 1),
            (3, 1, 2),
            (3, 3, 1),
            (4, 2, 11),
            (4, 3, 6),
            (5, 1, 24),
            (6, 3, 225),
            (7, 4, 735),
            (8, 5, 1960),
            (10, 5, 269325),
            (1000, 1000, 1),
            (1000, 1, 756641425),
            (1000, 999, 499500),
            (1000, 500, 761367694),
            (500, 250, 112330193),
        ],
    )
    def test_rearrange_sticks(self, n: int, k: int, expected: int):
        result = run_rearrange_sticks(Solution, n, k)
        assert_rearrange_sticks(result, expected)
