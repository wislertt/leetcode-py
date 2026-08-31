import pytest

from leetcode_py import logged_test

from .helpers import assert_is_monotonic, run_is_monotonic
from .solution import Solution


class TestMonotonicArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2, 3], True),
            ([6, 5, 4, 4], True),
            ([1, 3, 2], False),
            ([1], True),
            ([1, 1], True),
            ([1, 2], True),
            ([2, 1], True),
            ([5], True),
            ([1, 1, 1, 1], True),
            ([1, 2, 2, 3, 3, 4], True),
            ([5, 4, 4, 3, 1], True),
            ([1, 5, 3, 7], False),
            ([10], True),
            ([-3, -1, 0, 2], True),
            ([0, 0, 1, 0], False),
            ([100, -100], True),
            ([2, 2, 3, 2], False),
        ],
    )
    def test_is_monotonic(self, nums: list[int], expected: bool):
        result = run_is_monotonic(Solution, nums)
        assert_is_monotonic(result, expected)
