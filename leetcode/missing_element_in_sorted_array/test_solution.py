import pytest

from leetcode_py import logged_test

from .helpers import assert_missing_element, run_missing_element
from .solution import Solution


class TestMissingElementInSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([4, 7, 9, 10], 1, 5),
            ([4, 7, 9, 10], 3, 8),
            ([1, 2, 4], 3, 6),
            ([1], 5, 6),
            ([1, 2], 1, 3),
            ([5, 10, 15], 2, 7),
            ([1, 2, 3, 4, 5], 1, 6),
            ([7, 8, 9, 10, 20], 5, 15),
            ([1, 10000000], 9999999, 10000001),
            ([2, 3, 5, 7, 11], 4, 9),
            ([10, 20, 30, 40, 50, 60], 12, 23),
            ([1, 3], 1, 2),
        ],
    )
    def test_missing_element(self, nums: list[int], k: int, expected: int):
        result = run_missing_element(Solution, nums, k)
        assert_missing_element(result, expected)
