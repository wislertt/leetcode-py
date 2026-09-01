import pytest

from leetcode_py import logged_test

from .helpers import assert_find_buildings, run_find_buildings
from .solution import Solution


class TestBuildingsWithAnOceanView:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([4, 2, 3, 1], [0, 2, 3]),
            ([4, 3, 2, 1], [0, 1, 2, 3]),
            ([1, 3, 2, 4], [3]),
            ([1], [0]),
            ([2, 2, 2], [2]),
            ([5, 4, 3, 2, 1], [0, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], [4]),
            ([3, 1, 4, 1, 5, 9, 2, 6], [5, 7]),
            ([7, 7, 6, 5, 4, 8], [5]),
            ([1000000000, 1, 1000000000], [2]),
            ([2, 1, 2, 1], [2, 3]),
            ([1, 1], [1]),
            ([2, 3, 1, 2, 3, 4, 1, 5], [7]),
            ([9, 1, 1, 1, 9, 1, 8], [4, 6]),
            ([9, 3, 3, 1, 1], [0, 2, 4]),
            ([2, 5, 1, 7, 5, 3, 8, 3, 9, 7, 8], [8, 10]),
            ([2, 7, 6, 4, 2, 9, 10, 10, 3, 5, 8, 10], [11]),
            ([5, 8, 3, 4, 3, 5, 6, 9, 10, 10, 1, 9], [9, 11]),
            ([8, 5, 1, 2, 3, 1, 2, 7], [0, 7]),
            ([6, 1, 5, 9, 8, 1, 5, 7, 7, 1], [3, 4, 8, 9]),
        ],
    )
    def test_find_buildings(self, heights: list[int], expected: list[int]):
        result = run_find_buildings(Solution, heights)
        assert_find_buildings(result, expected)
