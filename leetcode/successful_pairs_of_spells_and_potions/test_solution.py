import pytest

from leetcode_py import logged_test

from .helpers import assert_successful_pairs, run_successful_pairs
from .solution import Solution


class TestSuccessfulPairsOfSpellsAndPotions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "spells, potions, success, expected",
        [
            ([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]),
            ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2]),
            ([1], [1], 1, [1]),
            ([1], [1], 2, [0]),
            ([100000], [100000], 10000000000, [1]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1, [5, 5, 5, 5, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 10000000000, [0, 0, 0, 0, 0]),
            ([5, 5, 5], [1, 2, 3, 4, 5], 25, [1, 1, 1]),
            ([2, 4, 8, 16], [1, 2, 4, 8, 16], 16, [2, 3, 4, 5]),
            ([10, 1], [10, 20, 30], 100, [3, 0]),
            ([20, 21, 5, 13], [10, 7, 13, 11], 16, [4, 4, 4, 4]),
            ([19, 25, 21, 29, 6], [31, 16], 16, [2, 2, 2, 2, 2]),
            ([36, 34], [26, 35, 36, 1], 5, [4, 4]),
            ([23, 31, 33], [14, 35, 10, 23], 1, [4, 4, 4]),
            ([5, 39, 10], [20, 38], 2, [2, 2, 2]),
            ([28, 13, 38], [1, 36, 2, 10, 28, 4], 7, [6, 6, 6]),
        ],
    )
    def test_successful_pairs(
        self, spells: list[int], potions: list[int], success: int, expected: list[int]
    ):
        result = run_successful_pairs(Solution, spells, potions, success)
        assert_successful_pairs(result, expected)
