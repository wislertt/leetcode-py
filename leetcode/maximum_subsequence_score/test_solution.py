import pytest

from leetcode_py import logged_test

from .helpers import assert_max_score, run_max_score
from .solution import Solution


class TestMaximumSubsequenceScore:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, k, expected",
        [
            ([1, 3, 3, 2], [2, 1, 3, 4], 3, 12),
            ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1, 30),
            ([1, 1], [1, 1], 1, 1),
            ([2, 1], [1, 2], 2, 3),
            ([5], [7], 1, 35),
            ([0, 0, 0], [0, 0, 0], 2, 0),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 2, 15),
            ([6, 10, 4], [9, 3, 8], 3, 60),
            ([2, 4, 6, 8], [1, 3, 5, 7], 3, 54),
            ([10, 2], [8, 0], 1, 80),
            ([2, 5, 8, 0, 1, 9, 6], [8, 3, 8, 9, 3, 10, 7], 6, 93),
            ([8, 5, 8, 3, 6, 8, 1, 7], [3, 4, 10, 5, 0, 10, 6, 0], 3, 102),
            ([4, 10], [7, 10], 1, 100),
            ([2, 7], [9, 0], 1, 18),
            ([6], [6], 1, 36),
            ([6, 9, 6, 9, 3], [9, 3, 7, 8, 10], 5, 99),
        ],
    )
    def test_max_score(self, nums1: list[int], nums2: list[int], k: int, expected: int):
        result = run_max_score(Solution, nums1, nums2, k)
        assert_max_score(result, expected)
