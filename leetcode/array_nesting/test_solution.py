import pytest

from leetcode_py import logged_test

from .helpers import assert_array_nesting, run_array_nesting
from .solution import Solution


class TestArrayNesting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 4, 0, 3, 1, 6, 2], 4),
            ([0, 1, 2], 1),
            ([0], 1),
            ([1, 0], 2),
            ([0, 2, 1], 2),
            ([3, 1, 2, 0], 2),
            ([2, 0, 4, 1, 3], 5),
            ([1, 2, 3, 4, 0], 5),
            ([5, 0, 1, 2, 3, 4], 6),
            ([4, 3, 2, 1, 0], 2),
            ([1, 0, 3, 2], 2),
            ([2, 6, 3, 0, 4, 5, 1], 3),
            ([2, 0, 1, 4, 6, 8, 3, 5, 7], 3),
            ([0, 1, 3, 2], 2),
            ([2, 6, 0, 5, 4, 1, 3], 4),
            ([6, 7, 1, 4, 2, 3, 0, 5], 6),
            ([1, 2, 3, 0], 4),
            ([3, 4, 0, 2, 1], 3),
        ],
    )
    def test_array_nesting(self, nums: list[int], expected: int):
        result = run_array_nesting(Solution, nums)
        assert_array_nesting(result, expected)
