import pytest

from leetcode_py import logged_test

from .helpers import assert_get_factors, run_get_factors
from .solution import Solution


class TestFactorCombinations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, []),
            (2, []),
            (3, []),
            (4, [[2, 2]]),
            (6, [[2, 3]]),
            (8, [[2, 4], [2, 2, 2]]),
            (12, [[3, 4], [2, 6], [2, 2, 3]]),
            (16, [[4, 4], [2, 8], [2, 2, 4], [2, 2, 2, 2]]),
            (24, [[4, 6], [3, 8], [2, 12], [2, 3, 4], [2, 2, 6], [2, 2, 2, 3]]),
            (27, [[3, 9], [3, 3, 3]]),
            (32, [[4, 8], [2, 16], [2, 4, 4], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2]]),
            (36, [[6, 6], [4, 9], [3, 12], [3, 3, 4], [2, 18], [2, 3, 6], [2, 2, 9], [2, 2, 3, 3]]),
            (37, []),
            (40, [[5, 8], [4, 10], [2, 20], [2, 4, 5], [2, 2, 10], [2, 2, 2, 5]]),
            (
                100,
                [
                    [10, 10],
                    [5, 20],
                    [4, 25],
                    [4, 5, 5],
                    [2, 50],
                    [2, 5, 10],
                    [2, 2, 25],
                    [2, 2, 5, 5],
                ],
            ),
        ],
    )
    def test_get_factors(self, n: int, expected: list[list[int]]):
        result = run_get_factors(Solution, n)
        assert_get_factors(result, expected)
