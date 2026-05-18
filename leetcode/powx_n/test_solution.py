import pytest

from leetcode_py import logged_test

from .helpers import assert_my_pow, run_my_pow
from .solution import Solution


class TestPowXN:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, n, expected",
        [
            (2.0, 10, 1024.0),
            (2.1, 3, 9.261),
            (2.0, -2, 0.25),
            (1.0, 0, 1.0),
            (0.5, 2, 0.25),
            (2.0, 1, 2.0),
            (3.0, 3, 27.0),
            (1.0, 100, 1.0),
            (0.0, 1, 0.0),
            (2.0, -1, 0.5),
            (10.0, 0, 1.0),
            (1.5, 2, 2.25),
            (0.5, -2, 4.0),
            (2.0, -3, 0.125),
            (1.0, -1, 1.0),
            (0.1, 3, 0.001),
        ],
    )
    def test_my_pow(self, x: float, n: int, expected: float):
        result = run_my_pow(Solution, x, n)
        assert_my_pow(result, expected)
