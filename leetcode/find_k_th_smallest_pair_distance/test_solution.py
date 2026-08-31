import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_distance_pair, run_smallest_distance_pair
from .solution import Solution


class TestFindKThSmallestPairDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 3, 1], 1, 0),
            ([1, 1, 1], 2, 0),
            ([1, 6, 1], 3, 5),
            ([0, 0, 0], 1, 0),
            ([1, 2, 3, 4], 6, 3),
            ([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18, 2),
            ([0, 1000000], 1, 1000000),
            ([5, 5, 5, 5], 6, 0),
            ([1, 2], 1, 1),
            ([2, 1], 1, 1),
            ([0, 10, 20, 30], 4, 20),
            ([4, 62, 100, 19, 3], 7, 59),
            ([1, 1, 1, 1, 1], 10, 0),
            ([10, 1, 10, 1], 4, 9),
        ],
    )
    def test_smallest_distance_pair(self, nums: list[int], k: int, expected: int):
        result = run_smallest_distance_pair(Solution, nums, k)
        assert_smallest_distance_pair(result, expected)
