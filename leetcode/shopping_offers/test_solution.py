import pytest

from leetcode_py import logged_test

from .helpers import assert_shopping_offers, run_shopping_offers
from .solution import Solution


class TestShoppingOffers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "price, special, needs, expected",
        [
            ([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2], 14),
            ([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1], 11),
            ([2, 3], [[1, 1, 10]], [2, 2], 10),
            ([2, 3], [[1, 1, 1]], [0, 0], 0),
            ([5], [[2, 8]], [4], 16),
            ([0, 3], [[1, 0, 0]], [2, 1], 3),
            ([3, 4], [[2, 2, 7]], [6, 6], 21),
            ([1, 1], [[1, 1, 5], [2, 0, 1]], [3, 3], 5),
            ([7], [[1, 5]], [0], 0),
            ([4, 5], [[1, 1, 6]], [3, 2], 16),
            ([1, 2, 3], [[1, 1, 1, 2], [0, 3, 0, 4]], [2, 4, 1], 7),
            ([9, 9], [[1, 1, 1]], [1, 1], 1),
            ([10, 10, 10], [[1, 1, 1, 25]], [2, 0, 2], 40),
            ([1, 1, 1, 1], [[1, 0, 0, 0, 0], [0, 1, 1, 0, 1]], [2, 2, 2, 2], 4),
            ([6], [[3, 14]], [5], 26),
            ([2, 2], [[1, 0, 3], [0, 2, 4], [1, 1, 5]], [3, 3], 12),
            ([1, 6, 0], [[2, 2, 2, 9]], [1, 2, 2], 13),
            ([4, 1, 7], [[1, 2, 2, 7]], [2, 2, 2], 11),
            ([0, 1], [[1, 0, 7], [2, 2, 7]], [0, 0], 0),
            ([0, 3, 6], [[1, 0, 0, 14], [0, 1, 1, 13], [1, 0, 0, 15]], [1, 3, 0], 9),
            ([10, 0, 0], [[0, 0, 2, 4]], [0, 2, 2], 0),
            ([9, 0], [[2, 0, 12], [0, 1, 12]], [3, 1], 21),
        ],
    )
    def test_shopping_offers(
        self, price: list[int], special: list[list[int]], needs: list[int], expected: int
    ):
        result = run_shopping_offers(Solution, price, special, needs)
        assert_shopping_offers(result, expected)
