import pytest

from leetcode_py import logged_test

from .helpers import assert_combination_sum_3, run_combination_sum_3
from .solution import Solution


class TestTestCombinationSumIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, k, n, expected",
        [
            (Solution, 3, 7, [[1, 2, 4]]),
            (Solution, 3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
            (Solution, 4, 1, []),
            (Solution, 2, 18, []),
            (Solution, 9, 45, [[1, 2, 3, 4, 5, 6, 7, 8, 9]]),
            (Solution, 9, 44, []),
            (Solution, 9, 1, []),
            (Solution, 2, 3, [[1, 2]]),
            (Solution, 2, 17, [[8, 9]]),
            (Solution, 4, 10, [[1, 2, 3, 4]]),
            (Solution, 4, 11, [[1, 2, 3, 5]]),
            (Solution, 5, 15, [[1, 2, 3, 4, 5]]),
            (Solution, 5, 16, [[1, 2, 3, 4, 6]]),
            (Solution, 6, 21, [[1, 2, 3, 4, 5, 6]]),
            (Solution, 7, 28, [[1, 2, 3, 4, 5, 6, 7]]),
            (Solution, 8, 36, [[1, 2, 3, 4, 5, 6, 7, 8]]),
            (Solution, 3, 45, []),
            (Solution, 3, 46, []),
            (Solution, 2, 4, [[1, 3]]),
            (Solution, 6, 22, [[1, 2, 3, 4, 5, 7]]),
            (Solution, 7, 20, []),
            (Solution, 8, 30, []),
        ],
    )
    def test_combination_sum_3(self, solution_class, k: int, n: int, expected: list[list[int]]):
        result = run_combination_sum_3(solution_class, k, n)
        assert_combination_sum_3(result, expected)
