import pytest

from leetcode_py import logged_test

from .helpers import assert_max_score, run_max_score
from .solution import Solution


class TestMaximizeScoreAfterNOperations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2], 1),
            ([3, 4, 6, 8], 11),
            ([1, 2, 3, 4, 5, 6], 14),
            ([1, 1], 1),
            ([2, 2], 2),
            ([1, 1000000], 1),
            ([4, 4, 4, 4], 12),
            ([1, 2, 3, 4], 5),
            ([7, 7, 7, 7, 7, 7], 42),
            ([10, 10, 10, 10], 30),
            ([2, 4, 6, 8, 10, 12, 14, 16], 56),
            ([1, 2, 3, 4, 5, 6, 7, 8], 28),
            ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 56),
            ([999983, 999979, 3, 5, 7, 11], 6),
            ([12, 18, 24, 36, 48, 60], 120),
            ([25, 5, 1, 11], 11),
            ([5, 12, 17, 21, 10, 25, 2, 22], 34),
            ([9, 24], 3),
            ([18, 19, 29, 7, 5, 10, 22, 8, 8, 10, 15, 22, 5, 28], 304),
            ([6, 7, 18, 17, 1, 24, 6, 3, 28, 17], 144),
        ],
    )
    def test_max_score(self, nums: list[int], expected: int):
        result = run_max_score(Solution, nums)
        assert_max_score(result, expected)
