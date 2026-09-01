import pytest

from leetcode_py import logged_test

from .helpers import assert_max_score, run_max_score
from .solution import Solution


class TestMaximumPointsYouCanObtainFromCards:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "card_points, k, expected",
        [
            ([1, 2, 3, 4, 5, 6, 1], 3, 12),
            ([2, 2, 2], 2, 4),
            ([9, 7, 7, 9, 7, 7, 9], 7, 55),
            ([1], 1, 1),
            ([5], 1, 5),
            ([1, 2], 1, 2),
            ([1, 2], 2, 3),
            ([2, 1, 100], 2, 102),
            ([100, 1, 2], 2, 102),
            ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202),
            ([11, 49, 100, 20, 86, 29, 72], 4, 232),
            ([1, 1000, 1, 1000, 1, 1000], 3, 2001),
            ([10, 10, 10, 1, 1, 10, 10, 10], 5, 50),
            ([1, 2, 3, 4, 5], 1, 5),
            ([744, 8747, 2957, 5952, 7396, 3151, 4613, 6795], 8, 40355),
            ([7896, 20, 6074], 1, 7896),
            ([9774, 7640, 95, 5445, 5668, 4826, 7208], 6, 40561),
            ([9055], 1, 9055),
            ([5225, 4514, 1115], 3, 10854),
            ([1645, 5408, 5758, 83], 4, 12894),
            ([4675, 2010, 9195], 1, 9195),
            ([7039, 3374, 2302, 3001], 3, 13414),
        ],
    )
    def test_max_score(self, card_points: list[int], k: int, expected: int):
        result = run_max_score(Solution, card_points, k)
        assert_max_score(result, expected)
