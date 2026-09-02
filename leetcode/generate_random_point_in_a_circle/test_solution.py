import pytest

from leetcode_py import logged_test

from .helpers import assert_rand_point, run_rand_point
from .solution import Solution


class TestGenerateRandomPointInACircle:
    @logged_test
    @pytest.mark.parametrize(
        "radius, x_center, y_center, seed, n",
        [
            (1.0, 0.0, 0.0, 0, 1),
            (1.0, 0.0, 0.0, 1, 2),
            (2.5, 1.0, -1.0, 2, 3),
            (1.0, 0.0, 0.0, 3, 5),
            (0.5, -3.0, 4.0, 4, 8),
            (10.0, 0.0, 0.0, 5, 10),
            (1.0, 10000000.0, -10000000.0, 6, 10),
            (100000000.0, 0.0, 0.0, 7, 10),
            (1.0, 0.0, 0.0, 8, 50),
            (3.0, 2.0, 2.0, 9, 100),
            (1.0, 0.0, 0.0, 10, 200),
            (7.0, -5.0, 5.0, 11, 500),
            (0.001, 100.0, -100.0, 13, 300),
            (1.0, 0.0, 0.0, 42, 150),
            (12.0, 0.5, 0.5, 14, 400),
            (1.0, 0.0, 0.0, 12, 2000),
        ],
    )
    def test_rand_point(self, radius: float, x_center: float, y_center: float, seed: int, n: int):
        result = run_rand_point(Solution, radius, x_center, y_center, seed, n)
        assert_rand_point(result, radius, x_center, y_center, n)
