import pytest

from leetcode_py import logged_test

from .helpers import assert_max_score_sightseeing_pair, run_max_score_sightseeing_pair
from .solution import Solution


class TestBestSightseeingPair:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "values, expected",
        [
            ([8, 1, 5, 2, 6], 11),
            ([1, 2], 2),
            ([1, 1000], 1000),
            ([1000, 1], 1000),
            ([2, 2, 2], 3),
            ([5, 5, 5, 5], 9),
            ([1, 3, 5], 7),
            ([10, 1, 1, 1, 10], 16),
            ([7, 7, 7, 1, 7], 13),
            ([4, 7, 3, 8, 2, 9], 15),
            ([100, 1, 100], 198),
            ([1, 1, 1, 1, 1, 1], 1),
        ],
    )
    def test_max_score_sightseeing_pair(self, values: list[int], expected: int):
        result = run_max_score_sightseeing_pair(Solution, values)
        assert_max_score_sightseeing_pair(result, expected)
