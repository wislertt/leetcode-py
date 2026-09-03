import pytest

from leetcode_py import logged_test

from .helpers import assert_powerful_integers, run_powerful_integers
from .solution import Solution


class TestPowerfulIntegers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, y, bound, expected",
        [
            (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
            (3, 5, 15, [2, 4, 6, 8, 10, 14]),
            (1, 1, 0, []),
            (1, 1, 1, []),
            (1, 1, 2, [2]),
            (1, 1, 1000000, [2]),
            (1, 2, 10, [2, 3, 5, 9]),
            (2, 1, 10, [2, 3, 5, 9]),
            (2, 3, 0, []),
            (2, 3, 1, []),
            (2, 3, 2, [2]),
            (2, 2, 5, [2, 3, 4, 5]),
            (2, 3, 30, [2, 3, 4, 5, 7, 9, 10, 11, 13, 17, 19, 25, 28, 29]),
            (5, 3, 100, [2, 4, 6, 8, 10, 14, 26, 28, 32, 34, 52, 82, 86]),
            (6, 6, 33, [2, 7, 12]),
            (4, 40, 200, [2, 5, 17, 41, 44, 56, 65, 104]),
            (7, 11, 500, [2, 8, 12, 18, 50, 60, 122, 128, 170, 344, 354, 464]),
            (100, 100, 1000000, [2, 101, 200, 10001, 10100, 20000]),
        ],
    )
    def test_powerful_integers(self, x: int, y: int, bound: int, expected: list[int]):
        result = run_powerful_integers(Solution, x, y, bound)
        assert_powerful_integers(result, expected)
