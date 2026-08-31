import pytest

from leetcode_py import logged_test

from .helpers import assert_can_place_flowers, run_can_place_flowers
from .solution import Solution


class TestCanPlaceFlowers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "flowerbed, n, expected",
        [
            ([1, 0, 0, 0, 1], 1, True),
            ([1, 0, 0, 0, 1], 2, False),
            ([0], 0, True),
            ([0], 1, True),
            ([1], 0, True),
            ([1], 1, False),
            ([0, 0], 1, True),
            ([0, 0], 2, False),
            ([0, 0, 0], 1, True),
            ([0, 0, 0], 2, True),
            ([0, 0, 0, 0], 2, True),
            ([0, 0, 0, 0], 3, False),
            ([1, 0, 0, 0, 0, 1], 1, True),
            ([1, 0, 0, 0, 0, 1], 2, False),
            ([0, 0, 1, 0, 0], 1, True),
            ([0, 0, 1, 0, 0], 2, True),
            ([0, 0, 1, 0, 0], 3, False),
        ],
    )
    def test_can_place_flowers(self, flowerbed: list[int], n: int, expected: bool):
        result = run_can_place_flowers(Solution, flowerbed, n)
        assert_can_place_flowers(result, expected)
