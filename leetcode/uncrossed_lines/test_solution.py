import pytest

from leetcode_py import logged_test

from .helpers import assert_max_uncrossed_lines, run_max_uncrossed_lines
from .solution import Solution


class TestUncrossedLines:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 4, 2], [1, 2, 4], 2),
            ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
            ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
            ([1], [1], 1),
            ([1], [2], 0),
            ([1, 2, 3], [3, 2, 1], 1),
            ([1, 2, 3, 4], [1, 2, 3, 4], 4),
            ([5, 5, 5], [5, 5], 2),
            ([1, 1, 2, 2], [2, 2, 1, 1], 2),
            ([10], [10], 1),
            ([1, 2, 1, 2], [2, 2, 1, 1], 2),
            ([7, 8, 9], [9, 8, 7, 7, 8, 9], 3),
        ],
    )
    def test_max_uncrossed_lines(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_max_uncrossed_lines(Solution, nums1, nums2)
        assert_max_uncrossed_lines(result, expected)
