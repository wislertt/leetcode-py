import pytest

from leetcode_py import logged_test

from .helpers import assert_min_swaps_couples, run_min_swaps_couples
from .solution import Solution


class TestCouplesHoldingHands:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "row, expected",
        [
            ([0, 2, 1, 3], 1),
            ([3, 2, 0, 1], 0),
            ([0, 1, 2, 3], 0),
            ([1, 0, 3, 2], 0),
            ([1, 2, 3, 0], 1),
            ([5, 4, 2, 6, 3, 1, 0, 7], 2),
            ([2, 0, 5, 4, 1, 3, 7, 6], 1),
            ([7, 6, 5, 4, 3, 2, 1, 0], 0),
            ([0, 3, 2, 1, 6, 5, 4, 7], 2),
            ([1, 4, 0, 5, 2, 7, 6, 3], 2),
            ([2, 3, 0, 1, 6, 7, 4, 5], 0),
            ([5, 3, 1, 0, 7, 2, 4, 6], 2),
            ([0, 9, 2, 7, 4, 5, 6, 3, 8, 1], 2),
            ([9, 1, 3, 2, 7, 4, 6, 0, 8, 5], 3),
            ([1, 3, 5, 7, 9, 0, 2, 4, 6, 8], 4),
            ([2, 1, 0, 3], 1),
            ([8, 7, 5, 3, 0, 6, 4, 1, 9, 2], 4),
            ([0, 5, 4, 3, 1, 2], 2),
            ([1, 6, 4, 5, 0, 2, 3, 7], 2),
            ([0, 3, 1, 2], 1),
        ],
    )
    def test_min_swaps_couples(self, row: list[int], expected: int):
        result = run_min_swaps_couples(Solution, row)
        assert_min_swaps_couples(result, expected)
