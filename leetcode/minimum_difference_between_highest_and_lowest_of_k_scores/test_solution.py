import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_difference, run_minimum_difference
from .solution import Solution


class TestMinimumDifferenceBetweenHighestAndLowestOfKScores:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([90], 1, 0),
            ([9, 4, 1, 7], 2, 2),
            ([9, 4, 1, 7], 3, 5),
            ([9, 4, 1, 7], 4, 8),
            ([1], 1, 0),
            ([5, 5, 5], 3, 0),
            ([0, 100000], 2, 100000),
            ([1, 3, 6, 10, 15], 3, 5),
            ([4, 8, 15, 16, 23, 42], 6, 38),
            ([2, 2, 2, 7, 7, 7], 4, 5),
            ([8, 3, 11, 5, 20, 1], 3, 4),
            ([100, 99, 101, 1, 2, 3], 2, 1),
            ([63, 99, 43, 39], 2, 4),
            ([49, 9, 31, 90, 84, 35, 6], 2, 3),
            ([67, 82], 2, 15),
            ([86, 24, 100, 23], 4, 77),
        ],
    )
    def test_minimum_difference(self, nums: list[int], k: int, expected: int):
        result = run_minimum_difference(Solution, nums, k)
        assert_minimum_difference(result, expected)
