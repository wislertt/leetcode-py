import pytest

from leetcode_py import logged_test

from .helpers import assert_pour_water, run_pour_water
from .solution import Solution


class TestPourWater:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, volume, k, expected",
        [
            ([2, 1, 1, 2, 1, 2, 2], 4, 3, [2, 2, 2, 3, 2, 2, 2]),
            ([1, 2, 3, 4], 2, 2, [2, 3, 3, 4]),
            ([3, 1, 3], 5, 1, [4, 4, 4]),
            ([2, 1, 1, 2, 1, 2, 2], 0, 3, [2, 1, 1, 2, 1, 2, 2]),
            ([5], 3, 0, [8]),
            ([0, 0, 0, 0], 7, 2, [2, 2, 2, 1]),
            ([4, 2, 1, 2, 4], 8, 2, [4, 4, 5, 4, 4]),
            ([1, 2, 3, 4, 5], 6, 0, [4, 4, 4, 4, 5]),
            ([5, 4, 3, 2, 1], 6, 4, [5, 4, 4, 4, 4]),
            ([2, 0, 2], 1, 1, [2, 1, 2]),
            ([3, 0, 3], 4, 1, [3, 4, 3]),
            ([1, 3, 2, 4, 1, 3, 1, 4], 5, 4, [1, 3, 2, 4, 4, 3, 3, 4]),
            ([9, 1, 9, 1, 9], 3, 1, [9, 4, 9, 1, 9]),
            ([0, 99, 0], 3, 0, [3, 99, 0]),
            ([2, 2, 2, 1, 2], 2, 0, [3, 2, 2, 2, 2]),
            ([1, 0, 2, 0, 1], 4, 2, [2, 2, 2, 1, 1]),
            ([7, 3, 5, 3, 7], 5, 2, [7, 5, 6, 5, 7]),
            ([0, 1, 0, 1, 0], 2, 2, [1, 1, 1, 1, 0]),
        ],
    )
    def test_pour_water(self, heights: list[int], volume: int, k: int, expected: list[int]):
        result = run_pour_water(Solution, heights, volume, k)
        assert_pour_water(result, expected)
