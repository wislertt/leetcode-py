import pytest

from leetcode_py import logged_test

from .helpers import assert_deck_revealed_increasing, run_deck_revealed_increasing
from .solution import Solution


class TestRevealCardsInIncreasingOrder:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "deck, expected",
        [
            ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7]),
            ([1, 1000], [1, 1000]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 3, 2]),
            ([1, 2, 3, 4], [1, 3, 2, 4]),
            ([7, 6, 5, 4, 3, 2, 1], [1, 6, 2, 5, 3, 7, 4]),
            ([10, 20, 30, 40, 50], [10, 50, 20, 40, 30]),
            ([1, 2, 3, 4, 5, 6], [1, 4, 2, 6, 3, 5]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 9, 2, 6, 3, 8, 4, 7, 5]),
        ],
    )
    def test_deck_revealed_increasing(self, deck: list[int], expected: list[int]):
        result = run_deck_revealed_increasing(Solution, deck)
        assert_deck_revealed_increasing(result, expected)
