import pytest

from leetcode_py import logged_test

from .helpers import assert_count_subarrays, run_count_subarrays
from .solution import Solution


class TestCountSubarraysWhereMaxElementAppearsAtLeastKTimes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 3, 2, 3, 3], 2, 6),
            ([1, 4, 2, 1], 3, 0),
            ([1, 1, 1], 1, 6),
            ([5], 1, 1),
            ([5], 2, 0),
            ([2, 2], 2, 1),
            ([1, 2, 3], 1, 3),
            ([3, 1, 3, 2, 3], 2, 5),
            ([4, 4, 1, 4], 2, 4),
            ([1, 2, 1, 2, 1], 2, 4),
            ([7, 7, 7, 7], 4, 1),
            ([7, 7, 7, 7], 5, 0),
            ([2, 1, 2, 2, 1, 2], 3, 5),
            ([1000000, 999999, 1000000, 1000000], 2, 4),
            ([1, 1, 2, 2, 1], 3, 0),
            ([3, 2, 2], 2, 0),
            ([1, 3, 3, 1, 1], 2, 6),
            ([3, 2, 2, 3, 2, 2], 3, 0),
        ],
    )
    def test_count_subarrays(self, nums: list[int], k: int, expected: int):
        result = run_count_subarrays(Solution, nums, k)
        assert_count_subarrays(result, expected)
