import pytest

from leetcode_py import logged_test

from .helpers import assert_combination_sum2, run_combination_sum2
from .solution import Solution


class TestCombinationSumII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "candidates, target, expected",
        [
            ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
            ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
            ([1], 1, [[1]]),
            ([1], 2, []),
            ([2], 1, []),
            ([1, 1], 2, [[1, 1]]),
            ([1, 1, 1], 2, [[1, 1]]),
            ([1, 1, 1, 1, 1], 3, [[1, 1, 1]]),
            ([1, 2], 4, []),
            ([1, 2, 3], 3, [[1, 2], [3]]),
            ([5, 3, 2, 1], 6, [[1, 2, 3], [1, 5]]),
            ([1, 2, 2, 2, 5], 5, [[1, 2, 2], [5]]),
            ([2, 2, 2], 4, [[2, 2]]),
            ([1, 1, 2, 2], 4, [[1, 1, 2], [2, 2]]),
        ],
    )
    def test_combination_sum2(self, candidates: list[int], target: int, expected: list[list[int]]):
        result = run_combination_sum2(Solution, candidates, target)
        assert_combination_sum2(result, expected)
