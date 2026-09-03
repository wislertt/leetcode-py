import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_line, run_longest_line
from .solution import Solution


class TestLongestLineOfConsecutiveOneInMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 3),
            ([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]], 4),
            ([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 2),
            ([[1]], 1),
            ([[0]], 0),
            ([[1, 0], [0, 1]], 2),
            ([[1], [1], [1], [1]], 4),
            ([[1, 1, 1, 1, 1]], 5),
            ([[0, 0, 0], [0, 0, 0]], 0),
            ([[1, 1], [1, 1]], 2),
            ([[1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]], 3),
            ([[0, 1], [1, 1], [0, 1]], 3),
            ([[1, 1, 0, 1, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]], 3),
            ([[0, 0, 1], [0, 1, 0], [1, 0, 0]], 3),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]], 3),
            ([[0, 1, 1, 1], [1, 0, 1, 1]], 3),
        ],
    )
    def test_longest_line(self, mat: list[list[int]], expected: int):
        result = run_longest_line(Solution, mat)
        assert_longest_line(result, expected)
