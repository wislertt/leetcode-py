import pytest

from leetcode_py import logged_test

from .helpers import assert_can_divide_into_subsequences, run_can_divide_into_subsequences
from .solution import Solution


class TestDivideArrayIntoIncreasingSequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 2, 3, 3, 4, 4], 3, True),
            ([5, 6, 6, 7, 8], 3, False),
            ([1, 1], 2, False),
            ([1, 1], 1, True),
            ([1], 1, True),
            ([1, 1, 1], 2, False),
            ([1, 1, 1, 2], 2, False),
            ([1, 2, 3, 4, 5], 5, True),
            ([1, 2, 3, 4, 5], 3, True),
            ([1, 1, 2, 2, 3, 3], 3, True),
            ([1, 1, 1, 1, 2], 3, False),
            ([1, 1, 1, 1, 2, 3], 4, False),
            ([1, 1, 1, 1, 2, 3], 2, False),
        ],
    )
    def test_can_divide_into_subsequences(self, nums: list[int], k: int, expected: bool):
        result = run_can_divide_into_subsequences(Solution, nums, k)
        assert_can_divide_into_subsequences(result, expected)
