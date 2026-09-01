import pytest

from leetcode_py import logged_test

from .helpers import assert_furthest_building, run_furthest_building
from .solution import Solution


class TestFurthestBuildingYouCanReach:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, bricks, ladders, expected",
        [
            ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
            ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
            ([14, 3, 19, 3], 17, 0, 3),
            ([1], 0, 0, 0),
            ([1, 2], 0, 0, 0),
            ([1, 2], 1, 0, 1),
            ([1, 2], 0, 1, 1),
            ([1, 2, 3, 4, 5], 3, 0, 3),
            ([1, 5, 1, 5, 1, 5], 0, 2, 4),
            ([3, 3, 3], 0, 0, 2),
            ([5, 4, 3, 2, 1], 0, 0, 4),
            ([1, 100], 99, 0, 1),
            ([1, 100], 100, 0, 1),
            ([1, 2, 3, 4], 0, 4, 3),
            ([2, 7, 4, 9, 1, 12], 8, 1, 4),
            ([10, 1, 10, 1, 10], 5, 1, 3),
            ([4, 3, 7, 1, 8, 10, 8], 1, 2, 4),
            ([3, 3, 10, 3, 7, 5, 3, 2, 1], 2, 9, 8),
            ([5, 5, 1], 15, 3, 2),
            ([8, 11, 8], 4, 2, 2),
            ([5, 11], 5, 0, 0),
            ([12, 6, 12, 9, 2], 11, 5, 4),
            ([2, 12, 3, 6, 1, 9, 7], 2, 3, 6),
            ([12, 11, 7], 5, 3, 2),
            ([10, 9, 10, 11, 2, 11], 9, 1, 5),
            ([6, 6, 4, 1, 10], 4, 4, 4),
            ([8, 8, 9, 4, 10, 7, 4, 3], 3, 4, 7),
            ([1, 8, 4, 3, 3, 12, 12], 11, 6, 6),
            ([10, 7, 8, 4, 12, 4], 6, 3, 5),
            ([12], 0, 1, 0),
            ([11, 12, 9, 10, 10, 5, 11], 6, 6, 6),
            ([6, 12, 5, 10, 5, 10, 2, 8], 7, 0, 2),
            ([8, 2, 6, 5, 11], 1, 3, 4),
            ([9, 5, 12, 2, 7, 8, 5, 11, 5], 9, 6, 8),
            ([7, 5, 6], 1, 0, 2),
            ([9, 2, 4, 9, 3, 7, 9], 3, 2, 5),
        ],
    )
    def test_furthest_building(self, heights: list[int], bricks: int, ladders: int, expected: int):
        result = run_furthest_building(Solution, heights, bricks, ladders)
        assert_furthest_building(result, expected)
