import pytest

from leetcode_py import logged_test

from .helpers import assert_beautiful_subsets, run_beautiful_subsets
from .solution import Solution


class TestTheNumberOfBeautifulSubsets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([2, 4, 6], 2, 4),
            ([1], 1, 1),
            ([1, 1], 1, 3),
            ([5, 3], 2, 2),
            ([1, 2, 3, 4], 1, 7),
            ([1, 2, 3, 4], 2, 8),
            ([1000, 500], 500, 2),
            ([10, 1, 10], 9, 4),
            ([7, 7, 7], 3, 7),
            ([1, 5, 9], 4, 4),
            ([2, 3], 1, 2),
            ([1000, 1000, 1], 999, 4),
            ([1, 8, 3, 10, 6, 9], 5, 35),
            ([2, 7], 1, 3),
            ([5, 10], 4, 3),
            ([5, 2, 10, 10, 3, 6], 1, 35),
            ([10, 3, 7, 9], 3, 11),
            ([9, 2, 9], 5, 7),
        ],
    )
    def test_beautiful_subsets(self, nums: list[int], k: int, expected: int):
        result = run_beautiful_subsets(Solution, nums, k)
        assert_beautiful_subsets(result, expected)
