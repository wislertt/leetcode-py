import pytest

from leetcode_py import logged_test

from .helpers import assert_min_sub_array_len, run_min_sub_array_len
from .solution import Solution


class TestMinimumSizeSubarraySum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, nums, expected",
        [
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
            (15, [1, 2, 3, 4, 5], 5),
            (100, [1, 1, 1, 1, 1, 1], 0),
            (1, [1], 1),
            (2, [1], 0),
            (3, [1, 1, 1], 3),
            (6, [10, 2, 3], 1),
            (11, [1, 2, 3, 4, 5], 3),
            (5, [1, 2, 3, 4, 5], 1),
            (7, [1, 1, 1, 1, 1, 1, 1], 7),
            (4, [4], 1),
            (10, [1, 2, 3, 4, 5], 3),
            (1, [1, 2, 3], 1),
        ],
    )
    def test_min_sub_array_len(self, target: int, nums: list[int], expected: int):
        result = run_min_sub_array_len(Solution, target, nums)
        assert_min_sub_array_len(result, expected)
