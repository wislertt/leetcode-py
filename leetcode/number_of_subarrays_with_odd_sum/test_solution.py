import pytest

from leetcode_py import logged_test

from .helpers import assert_num_of_subarrays, run_num_of_subarrays
from .solution import Solution


class TestNumberOfSubarraysWithOddSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 3, 5], 4),
            ([2, 4, 6], 0),
            ([1, 2, 3, 4, 5, 6, 7], 16),
            ([1], 1),
            ([2], 0),
            ([1, 2], 2),
            ([2, 1], 2),
            ([1, 1], 2),
            ([1, 1, 1, 1], 6),
            ([1, 2, 2, 2], 4),
            ([2, 2, 2, 1], 4),
            ([100, 100, 100], 0),
            ([100, 99], 2),
            ([7, 4, 3, 8, 5], 9),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),
            ([7, 36, 27, 69, 5, 82], 12),
            ([1, 68, 73, 14, 42, 64, 27, 77], 18),
            ([77, 27, 26, 64, 4, 9, 42, 38, 13, 24, 68, 40], 36),
            ([71, 79, 16, 1, 65, 81, 33, 45, 89, 59, 94, 40, 42, 58, 45], 63),
        ],
    )
    def test_num_of_subarrays(self, arr: list[int], expected: int):
        result = run_num_of_subarrays(Solution, arr)
        assert_num_of_subarrays(result, expected)
