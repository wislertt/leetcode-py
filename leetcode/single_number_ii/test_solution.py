import pytest

from leetcode_py import logged_test

from .helpers import assert_single_number, run_single_number
from .solution import Solution


class TestSingleNumberII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 2, 3, 2], 3),
            ([0, 1, 0, 1, 0, 1, 99], 99),
            ([1], 1),
            ([7, 7, 7, 8], 8),
            ([-1, -1, -1, -2], -2),
            ([-2147483648], -2147483648),
            ([2147483647], 2147483647),
            ([2147483647, 2147483647, 2147483647, -2147483648], -2147483648),
            ([-2147483648, -2147483648, -2147483648, 2147483647], 2147483647),
            ([0, 0, 0, -5], -5),
            ([100, 99, 100, 100], 99),
            ([1, 2, 3, 1, 2, 1, 2], 3),
            ([-334, -606, -606, -1836671566, -606, -334, -334], -1836671566),
            ([-721, -721, -721, 1983358728, -126, -126, -126], 1983358728),
            ([809424842, 833, -263, 833, -263, -263, 833], 809424842),
            ([485, -431203817, 485, 485], -431203817),
            ([938, 938, -1298594836, 859, 938, 859, 859], -1298594836),
            ([418, -1722992034, 418, 418], -1722992034),
        ],
    )
    def test_single_number(self, nums: list[int], expected: int):
        result = run_single_number(Solution, nums)
        assert_single_number(result, expected)
