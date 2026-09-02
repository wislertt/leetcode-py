import pytest

from leetcode_py import logged_test

from .helpers import assert_is_array_special, run_is_array_special
from .solution import Solution


class TestSpecialArrayI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1], True),
            ([2, 1, 4], True),
            ([4, 3, 1, 6], False),
            ([2], True),
            ([5], True),
            ([1, 2], True),
            ([2, 3], True),
            ([1, 1], False),
            ([4, 4], False),
            ([1, 2, 1, 2], True),
            ([2, 1, 2, 1], True),
            ([1, 2, 3], True),
            ([2, 3, 4], True),
            ([7, 8, 9, 10], True),
            ([1, 3], False),
            ([6, 2, 4], False),
            ([99, 100, 99], True),
            ([100, 1, 100, 1], True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
            ([1, 4, 2, 6], False),
            ([50, 51], True),
            ([3, 3, 3], False),
        ],
    )
    def test_is_array_special(self, nums: list[int], expected: bool):
        result = run_is_array_special(Solution, nums)
        assert_is_array_special(result, expected)
