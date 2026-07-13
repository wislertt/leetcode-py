import pytest

from leetcode_py import logged_test

from .helpers import assert_combine, run_combine
from .solution import Solution


class TestTestCombinations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, n, k, expected",
        [
            (Solution, 4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
            (Solution, 1, 1, [[1]]),
            (Solution, 2, 1, [[1], [2]]),
            (Solution, 3, 3, [[1, 2, 3]]),
            (Solution, 5, 1, [[1], [2], [3], [4], [5]]),
            (Solution, 3, 2, [[1, 2], [1, 3], [2, 3]]),
            (Solution, 4, 1, [[1], [2], [3], [4]]),
            (Solution, 4, 3, [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]),
            (Solution, 4, 4, [[1, 2, 3, 4]]),
            (Solution, 5, 5, [[1, 2, 3, 4, 5]]),
            (
                Solution,
                5,
                3,
                [
                    [1, 2, 3],
                    [1, 2, 4],
                    [1, 2, 5],
                    [1, 3, 4],
                    [1, 3, 5],
                    [1, 4, 5],
                    [2, 3, 4],
                    [2, 3, 5],
                    [2, 4, 5],
                    [3, 4, 5],
                ],
            ),
            (Solution, 2, 2, [[1, 2]]),
            (
                Solution,
                6,
                2,
                [
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [1, 5],
                    [1, 6],
                    [2, 3],
                    [2, 4],
                    [2, 5],
                    [2, 6],
                    [3, 4],
                    [3, 5],
                    [3, 6],
                    [4, 5],
                    [4, 6],
                    [5, 6],
                ],
            ),
            (
                Solution,
                5,
                4,
                [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]],
            ),
            (Solution, 3, 1, [[1], [2], [3]]),
        ],
    )
    def test_combine(self, solution_class, n: int, k: int, expected: list[list[int]]):
        result = run_combine(solution_class, n, k)
        assert_combine(result, expected)
