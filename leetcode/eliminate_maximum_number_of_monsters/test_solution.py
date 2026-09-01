import pytest

from leetcode_py import logged_test

from .helpers import assert_eliminate_maximum, run_eliminate_maximum
from .solution import Solution


class TestEliminateMaximumNumberOfMonsters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "dist, speed, expected",
        [
            ([1, 3, 4], [1, 1, 1], 3),
            ([1, 1, 2, 3], [1, 1, 1, 1], 1),
            ([3, 2, 4], [5, 3, 2], 1),
            ([1], [1], 1),
            ([100000], [100000], 1),
            ([100000], [1], 1),
            ([1, 1], [1, 1], 1),
            ([2, 2], [1, 1], 2),
            ([5, 4, 3, 2, 1], [1, 1, 1, 1, 1], 5),
            ([1, 3, 5, 7], [1, 1, 1, 1], 4),
            ([4, 2, 3], [1, 1, 1], 3),
            ([1, 2], [1, 1], 2),
            ([1, 1, 1], [1, 1, 1], 1),
            ([2, 3, 4, 5], [1, 1, 1, 1], 4),
            ([7, 8, 9, 10], [2, 3, 4, 5], 4),
            ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5], 1),
            ([3, 1, 4, 1, 5], [2, 7, 1, 8, 2], 1),
            ([9, 9, 9, 9], [10, 1, 5, 3], 4),
            ([8], [2], 1),
            ([1, 3, 8, 1, 4, 1, 8, 4], [5, 1, 1, 3, 6, 5, 1, 4], 1),
            ([3, 6, 3, 6], [3, 6, 4, 4], 1),
            ([2], [5], 1),
            ([1], [5], 1),
            ([8], [4], 1),
            ([7, 10, 4, 5, 9, 1], [1, 6, 5, 5, 4, 4], 1),
            ([2, 10, 7, 3], [2, 6, 5, 4], 1),
            ([8], [5], 1),
            ([1, 7], [4, 5], 2),
            ([1, 6, 3, 4, 3], [6, 3, 3, 1, 3], 1),
            ([5, 5, 2], [6, 6, 4], 1),
            ([3, 7, 10, 8, 5, 2], [5, 3, 6, 4, 4, 5], 1),
            ([2, 5, 1, 3, 7, 5, 6], [1, 5, 2, 3, 4, 1, 5], 1),
            ([5, 1, 2, 8, 6, 7, 4, 4, 1, 8], [5, 4, 6, 5, 1, 5, 6, 1, 7, 8], 1),
            ([1, 5, 9, 9, 1, 2, 2, 8, 6, 7], [8, 9, 9, 9, 4, 6, 6, 8, 9, 7], 1),
        ],
    )
    def test_eliminate_maximum(self, dist: list[int], speed: list[int], expected: int):
        result = run_eliminate_maximum(Solution, dist, speed)
        assert_eliminate_maximum(result, expected)
