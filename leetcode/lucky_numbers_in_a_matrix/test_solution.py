import pytest

from leetcode_py import logged_test

from .helpers import assert_lucky_numbers, run_lucky_numbers
from .solution import Solution


class TestLuckyNumbersInAMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
            ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
            ([[7, 8], [1, 2]], [7]),
            ([[5]], [5]),
            ([[2, 1], [4, 3]], [3]),
            ([[10, 20, 30], [40, 50, 60], [70, 80, 90]], [70]),
            ([[9, 8, 7], [6, 5, 4], [3, 2, 1]], [7]),
            ([[100]], [100]),
            ([[1, 3], [2, 4]], [2]),
            ([[5, 6], [7, 8]], [7]),
            ([[4, 3, 2], [1, 5, 6]], []),
            ([[23], [98], [32], [52]], [98]),
            ([[27, 33], [31, 45], [52, 99]], [52]),
            ([[32, 51, 8], [65, 39, 24], [70, 44, 64]], []),
            ([[31], [51], [17]], [51]),
            ([[37, 35, 63], [94, 97, 57], [39, 46, 86], [27, 12, 16]], []),
        ],
    )
    def test_lucky_numbers(self, matrix: list[list[int]], expected: list[int]):
        result = run_lucky_numbers(Solution, matrix)
        assert_lucky_numbers(result, expected)
