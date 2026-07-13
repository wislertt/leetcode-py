import pytest

from leetcode_py import logged_test

from .helpers import assert_my_sqrt, run_my_sqrt
from .solution import Solution


class TestTestSqrtx:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, x, expected",
        [
            (Solution, 4, 2),
            (Solution, 8, 2),
            (Solution, 0, 0),
            (Solution, 1, 1),
            (Solution, 2, 1),
            (Solution, 3, 1),
            (Solution, 6, 2),
            (Solution, 7, 2),
            (Solution, 9, 3),
            (Solution, 15, 3),
            (Solution, 16, 4),
            (Solution, 25, 5),
            (Solution, 26, 5),
            (Solution, 99, 9),
            (Solution, 100, 10),
            (Solution, 2147483647, 46340),
            (Solution, 2147395600, 46340),
            (Solution, 2147395599, 46339),
        ],
    )
    def test_my_sqrt(self, solution_class, x: int, expected: int):
        result = run_my_sqrt(solution_class, x)
        assert_my_sqrt(result, expected)
