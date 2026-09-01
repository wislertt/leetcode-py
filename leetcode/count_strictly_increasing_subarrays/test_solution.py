import pytest

from leetcode_py import logged_test

from .helpers import assert_count_strictly_increasing, run_count_strictly_increasing
from .solution import Solution


class TestCountStrictlyIncreasingSubarrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 5, 4, 4, 6], 10),
            ([1, 2, 3, 4, 5], 15),
            ([1], 1),
            ([5, 5], 2),
            ([1, 2], 3),
            ([2, 1], 2),
            ([3, 2, 1], 3),
            ([1, 2, 3], 6),
            ([1, 3, 2, 4], 6),
            ([10, 20, 30, 10, 20], 9),
            ([7, 7, 7, 7], 4),
            ([1, 2, 1, 2, 1, 2], 9),
            ([1000000, 1, 1000000], 4),
            ([4, 5, 6, 6, 7, 8, 1, 2], 15),
            ([7, 11], 3),
            ([13, 1, 8, 9, 19, 1], 12),
            ([2, 4, 14, 14, 11, 3, 8, 10, 12, 13, 16, 12], 30),
            ([11, 8, 11, 4, 15, 8, 15, 7, 6], 12),
            ([13, 7, 20, 17, 4, 1, 17, 15, 6], 11),
            ([3, 11, 6, 10, 10], 7),
        ],
    )
    def test_count_strictly_increasing(self, nums: list[int], expected: int):
        result = run_count_strictly_increasing(Solution, nums)
        assert_count_strictly_increasing(result, expected)
