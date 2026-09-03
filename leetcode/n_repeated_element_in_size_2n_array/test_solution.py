import pytest

from leetcode_py import logged_test

from .helpers import assert_repeated_n_times, run_repeated_n_times
from .solution import Solution


class TestNRepeatedElementInSize2NArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 3], 3),
            ([2, 1, 2, 5, 3, 2], 2),
            ([5, 1, 5, 2, 5, 3, 5, 4], 5),
            ([9, 5, 9, 7], 9),
            ([3, 4, 4, 8], 4),
            ([0, 0, 1, 2], 0),
            ([7, 8, 9, 7], 7),
            ([3, 1, 2, 3], 3),
            ([4, 4, 1, 2], 4),
            ([6, 2, 3, 6], 6),
            ([1, 2, 1, 3], 1),
            ([1, 2, 3, 3, 4, 3], 3),
            ([1, 2, 3, 4, 5, 5, 5, 5, 5, 6], 5),
            ([10, 10, 0, 1, 2, 10, 10, 3, 4, 10], 10),
            ([10000, 9999, 10000, 42], 10000),
            ([2, 3, 4, 5, 2, 6, 2, 2, 2, 8, 9, 2], 2),
            ([500, 0, 1, 500, 2, 500, 3, 500], 500),
            ([8, 8, 8, 8, 8, 1, 2, 3, 4, 5], 8),
        ],
    )
    def test_repeated_n_times(self, nums: list[int], expected: int):
        result = run_repeated_n_times(Solution, nums)
        assert_repeated_n_times(result, expected)
