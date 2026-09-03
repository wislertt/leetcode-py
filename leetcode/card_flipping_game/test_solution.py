import pytest

from leetcode_py import logged_test

from .helpers import assert_flipgame, run_flipgame
from .solution import Solution


class TestCardFlippingGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "fronts, backs, expected",
        [
            ([1, 2, 4, 4, 7], [1, 3, 4, 1, 3], 2),
            ([1], [1], 0),
            ([1, 2], [2, 1], 1),
            ([1, 1], [1, 1], 0),
            ([2, 2], [1, 1], 1),
            ([1, 2, 3], [1, 2, 3], 0),
            ([5], [3], 3),
            ([3, 7, 5], [3, 7, 5], 0),
            ([4, 5], [4, 6], 5),
            ([1, 1, 2], [1, 3, 2], 3),
            ([100, 200], [200, 100], 100),
            ([7], [6], 6),
            ([8, 5], [7, 2], 2),
            ([4, 7, 1, 5, 3], [4, 6, 2, 9, 7], 1),
            ([3, 8, 3, 9], [9, 7, 4, 8], 3),
            ([1], [9], 1),
            ([2, 3, 2, 5, 4], [1, 2, 7, 8, 2], 1),
            ([1, 4, 7, 2, 4], [5, 3, 7, 9, 6], 1),
            ([7, 1, 8, 2, 5, 3], [1, 1, 1, 5, 4, 8], 2),
        ],
    )
    def test_flipgame(self, fronts: list[int], backs: list[int], expected: int):
        result = run_flipgame(Solution, fronts, backs)
        assert_flipgame(result, expected)
