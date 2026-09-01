import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_index, run_minimum_index
from .solution import Solution


class TestMinimumIndexOfAValidSplit:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2, 2], 2),
            ([2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4),
            ([3, 3, 3, 3, 7, 2, 2], -1),
            ([7], -1),
            ([4, 4], 0),
            ([1, 2, 1], -1),
            ([1, 2, 2], -1),
            ([5, 5, 5, 1], 0),
            ([1000000000, 1, 1000000000], -1),
            ([1, 1, 2, 2, 1], -1),
            ([2, 2, 1, 1, 1, 1], 4),
            ([9, 3, 3, 9, 3, 3, 9], -1),
            ([9, 5, 5, 5, 5, 5, 5, 5, 9, 9, 3], 2),
            ([8, 3, 3], -1),
            ([2, 8, 5, 8, 8, 8, 8], 4),
            ([2, 5, 5, 5, 5, 5, 5, 3, 9, 5, 5, 6], 2),
            ([9, 7, 7, 7, 7, 7, 7, 7, 9], 2),
            ([6, 7, 5, 5, 6, 5, 5, 5, 1, 3, 5], -1),
            ([4, 7, 7, 7, 7, 7], 2),
            ([6, 4, 7, 4, 4, 4, 4, 4], 4),
            ([9, 5, 5, 5, 5, 5, 5, 5], 2),
            ([6, 7, 7, 7, 7, 5, 7, 7], 2),
            ([9, 8, 8, 9, 8, 8, 5, 8, 9, 8, 8, 8], 2),
            ([5, 1, 9, 1, 1, 1], 4),
            ([5, 2, 8, 2, 2, 2, 2, 2, 2], 4),
            ([9, 5, 5, 1, 5, 5, 8, 5, 4], -1),
            ([5, 7, 7, 7, 7, 7, 6, 7, 7, 9, 7], 2),
        ],
    )
    def test_minimum_index(self, nums: list[int], expected: int):
        result = run_minimum_index(Solution, nums)
        assert_minimum_index(result, expected)
