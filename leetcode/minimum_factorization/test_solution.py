import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_factorization, run_smallest_factorization
from .solution import Solution


class TestMinimumFactorization:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (48, 68),
            (15, 35),
            (1, 1),
            (2, 2),
            (9, 9),
            (10, 25),
            (13, 0),
            (128, 288),
            (300, 2556),
            (720, 2589),
            (1073741824, 0),
            (999999937, 0),
            (999999999, 0),
            (2147483646, 0),
        ],
    )
    def test_smallest_factorization(self, num: int, expected: int):
        result = run_smallest_factorization(Solution, num)
        assert_smallest_factorization(result, expected)
