import pytest

from leetcode_py import logged_test

from .helpers import assert_check_possibility, run_check_possibility
from .solution import Solution


class TestNonDecreasingArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 2, 3], True),
            ([4, 2, 1], False),
            ([1], True),
            ([1, 2, 3], True),
            ([3, 2, 1], False),
            ([2, 2, 2], True),
            ([1, 3, 2], True),
            ([3, 1, 2], True),
            ([1, 4, 2, 3], True),
            ([3, 4, 2, 3], False),
            ([5, 7, 1, 8], True),
            ([1, 2, 5, 3, 5], True),
            ([1, 1, 1, 1], True),
            ([-1, -2, -3], False),
            ([2, 3, 3, 2, 4], True),
            ([1, 5, 4, 6, 7, 10, 8], False),
            ([10, 1, 11, 2, 12], False),
        ],
    )
    def test_check_possibility(self, nums: list[int], expected: bool):
        result = run_check_possibility(Solution, nums)
        assert_check_possibility(result, expected)
