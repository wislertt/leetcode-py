from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_asteroid_collision, run_asteroid_collision
from .solution import Solution


class TestAsteroidCollision:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("asteroids, expected", [])
    def test_asteroid_collision(self, asteroids: List[int], expected: List[int]):
        result = run_asteroid_collision(Solution, asteroids)
        assert_asteroid_collision(result, expected)
