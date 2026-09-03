import pytest

from leetcode_py import logged_test

from .helpers import assert_advantage_count, run_advantage_count
from .solution import Solution


class TestAdvantageShuffle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([2, 7, 11, 15], [1, 10, 4, 11], 4),
            ([12, 24, 8, 32], [13, 25, 32, 11], 3),
            ([1, 2, 3, 4], [1, 2, 3, 4], 3),
            ([1], [1], 0),
            ([5], [1], 1),
            ([0, 0, 0], [0, 0, 0], 0),
            ([2, 0, 4, 1, 2], [1, 3, 0, 0, 2], 4),
            ([9, 1, 6, 3], [2, 2, 2, 2], 3),
            ([1, 3, 5, 7], [2, 4, 6, 8], 3),
            ([1000000000, 0], [0, 1000000000], 1),
            ([7, 7, 7, 7], [7, 7, 7, 7], 0),
            ([4, 11, 10, 1], [1, 10, 11, 4], 3),
            ([2, 7], [8, 9], 0),
            ([5, 5, 5], [1, 2, 3], 3),
            ([3, 1, 2], [4, 1, 1], 2),
            ([14, 14], [1, 11], 2),
            ([19, 10, 12], [7, 19, 14], 2),
            ([15, 20], [12, 15], 2),
            ([17], [11], 1),
            ([14, 2, 3, 6, 16, 19], [6, 4, 12, 12, 20, 18], 4),
        ],
    )
    def test_advantage_count(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_advantage_count(Solution, nums1, nums2)
        assert_advantage_count(result, expected)
