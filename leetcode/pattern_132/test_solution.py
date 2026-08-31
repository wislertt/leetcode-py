import pytest

from leetcode_py import logged_test

from .helpers import assert_find_132pattern, run_find_132pattern
from .solution import Solution


class TestPattern132:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], False),
            ([3, 1, 4, 2], True),
            ([-1, 3, 2, 0], True),
            ([1], False),
            ([1, 2], False),
            ([1, 1, 1], False),
            ([3, 2, 1], False),
            ([1, 2, 0], False),
            ([1, 0, 2], False),
            ([2, 1, 3, 0], False),
            ([-2, 1, 1], False),
            ([1, 4, 3], True),
            ([3, 5, 0, 3, 4], True),
            ([1, 3, 2], True),
            ([2, 3, 1], False),
            ([8, 10, 4, 6], False),
            ([5, 4, 3, 2, 1], False),
            ([1, 2, 3, 4, 5, 6, 7, 0], False),
        ],
    )
    def test_find_132pattern(self, nums: list[int], expected: bool):
        result = run_find_132pattern(Solution, nums)
        assert_find_132pattern(result, expected)
