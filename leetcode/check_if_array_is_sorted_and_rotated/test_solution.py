import pytest

from leetcode_py import logged_test

from .helpers import assert_check, run_check
from .solution import Solution


class TestCheckIfArrayIsSortedAndRotated:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 4, 5, 1, 2], True),
            ([2, 1, 3, 4], False),
            ([1, 2, 3], True),
            ([1], True),
            ([2, 1], True),
            ([1, 2], True),
            ([3, 4, 5, 1, 2, 6], False),
            ([2, 2, 2], True),
            ([1, 1, 1, 1], True),
            ([2, 1, 2, 2], True),
            ([1, 2, 3, 4, 5], True),
            ([5, 4, 3, 2, 1], False),
            ([3, 1, 2], True),
            ([1, 3, 2], False),
            ([2, 2, 2, 1, 2], True),
            ([6, 10, 6], True),
            ([6, 100, 13, 34], False),
            ([67, 71, 73], True),
            ([85, 21], True),
            ([34], True),
            ([48, 30, 98, 30, 98, 82, 9, 35], False),
            ([14, 43, 78], True),
            ([28, 16], True),
            ([72], True),
        ],
    )
    def test_check(self, nums: list[int], expected: bool):
        result = run_check(Solution, nums)
        assert_check(result, expected)
