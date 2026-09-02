import pytest

from leetcode_py import logged_test

from .helpers import assert_divide_array_into_equal_pairs, run_divide_array_into_equal_pairs
from .solution import Solution


class TestDivideArrayIntoEqualPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 2, 3, 2, 2, 2], True),
            ([1, 2, 3, 4], False),
            ([1, 1], True),
            ([1, 2], False),
            ([5, 5, 5, 5], True),
            ([1, 2, 3, 1], False),
            ([10, 10], True),
            ([1, 1, 2, 2, 3, 3], True),
            ([1, 1, 1, 1, 2, 2], True),
            ([1, 1, 1, 2, 2, 2], False),
            ([500, 500], True),
            ([1, 500], False),
            ([2, 2, 2, 2, 3, 3, 4, 4], True),
            ([1, 1, 1, 1, 1, 1], True),
            ([448, 460, 362, 448, 460, 362, 211, 211], True),
            ([443, 225, 443, 225], True),
            ([80, 383, 131, 131, 80, 383], True),
            ([491, 395, 491, 395, 321, 321], True),
        ],
    )
    def test_divide_array_into_equal_pairs(self, nums: list[int], expected: bool):
        result = run_divide_array_into_equal_pairs(Solution, nums)
        assert_divide_array_into_equal_pairs(result, expected)
