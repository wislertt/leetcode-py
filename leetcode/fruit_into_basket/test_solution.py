import pytest

from leetcode_py import logged_test

from .helpers import assert_total_fruit, run_total_fruit
from .solution import Solution


class TestFruitIntoBasket:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "fruits, expected",
        [
            ([1, 2, 1], 3),
            ([0, 1, 2, 2], 3),
            ([1, 2, 3, 2, 2], 4),
            ([0], 1),
            ([0, 0], 2),
            ([0, 1], 2),
            ([3, 3, 3, 3, 3], 5),
            ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5),
            ([0, 1, 6, 6, 4, 4, 6], 5),
            ([0, 0, 1, 1, 0], 5),
            ([1, 0, 0, 2, 2, 0], 5),
            ([0, 1, 2, 3, 4], 2),
            ([2, 2, 2, 2, 1, 1, 3, 3], 6),
            ([5, 5, 5, 1, 1, 1, 5, 5], 8),
            ([0, 1, 2], 2),
        ],
    )
    def test_total_fruit(self, fruits: list[int], expected: int):
        result = run_total_fruit(Solution, fruits)
        assert_total_fruit(result, expected)
