import pytest

from leetcode_py import logged_test

from .helpers import assert_fib, run_fib
from .solution import Solution


class TestFibonacciNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, 1),
            (3, 2),
            (4, 3),
            (0, 0),
            (1, 1),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
            (11, 89),
            (12, 144),
            (15, 610),
            (18, 2584),
            (20, 6765),
            (25, 75025),
            (30, 832040),
        ],
    )
    def test_fib(self, n: int, expected: int):
        result = run_fib(Solution, n)
        assert_fib(result, expected)
