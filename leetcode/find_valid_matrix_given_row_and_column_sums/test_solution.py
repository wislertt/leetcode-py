import pytest

from leetcode_py import logged_test

from .helpers import assert_restore_matrix, run_restore_matrix
from .solution import Solution


class TestFindValidMatrixGivenRowAndColumnSums:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "row_sum, col_sum, expected",
        [
            ([3, 8], [4, 7], [[3, 0], [1, 7]]),
            ([5, 7, 10], [8, 6, 8], [[0, 5, 0], [6, 1, 0], [2, 0, 8]]),
            ([1], [1], [[1]]),
            ([0], [0], [[0]]),
            ([4], [2, 2], [[2, 2]]),
            ([2, 2], [4], [[2], [2]]),
            ([0, 5], [5, 0], [[0, 0], [5, 0]]),
            ([1, 2, 3], [2, 2, 2], [[1, 0, 0], [1, 1, 0], [0, 1, 2]]),
            ([10, 10, 10], [30], [[10], [10], [10]]),
            ([100000000], [100000000], [[100000000]]),
            ([1, 0, 1], [2, 0, 0], [[1, 0, 0], [0, 0, 0], [1, 0, 0]]),
            ([6, 6], [3, 3, 3, 3], [[3, 3, 0, 0], [0, 0, 3, 3]]),
            (
                [100000000, 100000000, 100000000],
                [100000000, 100000000, 100000000],
                [[100000000, 0, 0], [0, 100000000, 0], [0, 0, 100000000]],
            ),
            ([99999999, 1], [100000000], [[99999999], [1]]),
            ([2, 3, 4, 5], [1, 4, 9], [[1, 1, 0], [0, 3, 0], [0, 0, 4], [0, 0, 5]]),
            ([6, 11, 3], [17, 3], [[6, 0], [11, 0], [0, 3]]),
            (
                [12, 4, 5, 7, 5],
                [3, 27, 3, 0],
                [[3, 9, 0, 0], [0, 4, 0, 0], [0, 5, 0, 0], [0, 7, 0, 0], [0, 2, 3, 0]],
            ),
            ([10, 8], [1, 6, 11], [[1, 6, 3], [0, 0, 8]]),
            ([6, 12], [2, 13, 1, 2], [[2, 4, 0, 0], [0, 9, 1, 2]]),
        ],
    )
    def test_restore_matrix(
        self, row_sum: list[int], col_sum: list[int], expected: list[list[int]]
    ):
        result = run_restore_matrix(Solution, row_sum, col_sum)
        assert_restore_matrix(result, row_sum, col_sum, expected)
