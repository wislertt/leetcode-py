import pytest

from leetcode_py import logged_test

from .helpers import assert_solve_n_queens, assert_solve_n_queens_solution_count, run_solve_n_queens
from .solution import Solution


class TestNQueens:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, [["Q"]]),
            (2, []),
            (3, []),
            (4, [["..Q.", "Q...", "...Q", ".Q.."], [".Q..", "...Q", "Q...", "..Q."]]),
            (
                5,
                [
                    ["....Q", "..Q..", "Q....", "...Q.", ".Q..."],
                    ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
                    ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
                    ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
                    ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
                    ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
                    [".Q...", "....Q", "..Q..", "Q....", "...Q."],
                    [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
                    ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
                    ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
                ],
            ),
            (
                6,
                [
                    ["....Q.", "..Q...", "Q.....", ".....Q", "...Q..", ".Q...."],
                    ["...Q..", "Q.....", "....Q.", ".Q....", ".....Q", "..Q..."],
                    ["..Q...", ".....Q", ".Q....", "....Q.", "Q.....", "...Q.."],
                    [".Q....", "...Q..", ".....Q", "Q.....", "..Q...", "....Q."],
                ],
            ),
        ],
    )
    def test_solve_n_queens(self, n: int, expected: list[list[str]]):
        result = run_solve_n_queens(Solution, n)
        assert_solve_n_queens(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "n, expected_count", [(4, 2), (5, 10), (6, 4), (7, 40), (8, 92), (9, 352)]
    )
    def test_solve_n_queens_solution_count(self, n: int, expected_count: int):
        result = run_solve_n_queens(Solution, n)
        assert_solve_n_queens_solution_count(result, expected_count)
