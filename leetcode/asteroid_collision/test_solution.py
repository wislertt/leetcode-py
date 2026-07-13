import pytest

from leetcode_py import logged_test

from .helpers import assert_asteroid_collision, run_asteroid_collision
from .solution import Solution


class TestAsteroidCollision:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "asteroids, expected",
        [
            ([5, 10, -5], [5, 10]),
            ([8, -8], []),
            ([10, 2, -5], [10]),
            ([3, 5, -6, 2, -1, 4], [-6, 2, 4]),
            ([-2, -1, 1, 2], [-2, -1, 1, 2]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([-1, -2, -3], [-1, -2, -3]),
            ([5, 5, -5], [5]),
            ([5, 10, -5, -10], [5]),
            ([10, 5, -5], [10]),
            ([-2, 2, -1, -2], [-2]),
            ([1, -2, -3], [-2, -3]),
            ([2, -1, -2], []),
            ([5, -5], []),
            ([-1, 5, -5, 1], [-1, 1]),
        ],
    )
    def test_asteroid_collision(self, asteroids: list[int], expected: list[int]):
        result = run_asteroid_collision(Solution, asteroids)
        assert_asteroid_collision(result, expected)
