import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_pairs, run_reverse_pairs
from .solution import Solution


class TestReversePairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 2, 3, 1], 2),
            ([2, 4, 3, 5, 1], 3),
            ([1], 0),
            ([2, 1], 0),
            ([3, 1], 1),
            ([1, 2], 0),
            ([2, 1, 3], 0),
            ([1, 1, 1, 1], 0),
            ([5, 4, 3, 2, 1], 4),
            ([1, 2, 3, 4, 5], 0),
            ([0, -1, -2], 3),
            ([-1, -1, -1], 3),
            ([2147483647, -2147483648], 1),
            ([-2147483648, 2147483647], 0),
            ([2147483647, 2147483647, -2147483648], 2),
            ([-2147483648, 0, 2147483647], 0),
            ([-194, -914, -249, -815, 914, 183, 617, 904, 265], 9),
            ([-853, -972, -519, 694, 822, 835, 682], 3),
            ([378, 284, 745, -747, 404], 3),
            ([-762, 448, 751, -367, 284], 3),
            ([899, 69, -824, 490, 548, -228], 7),
            ([-258, 660, 872, -466, 807, -421, -222, 836, -660], 21),
        ],
    )
    def test_reverse_pairs(self, nums: list[int], expected: int):
        result = run_reverse_pairs(Solution, nums)
        assert_reverse_pairs(result, expected)
