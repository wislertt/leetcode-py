import pytest

from leetcode_py import logged_test

from .helpers import assert_copy_random_list, run_copy_random_list
from .solution import Solution


class TestCopyListWithRandomPointer:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nodes, expected",
        [
            (
                [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
                [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            ),
            ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
            ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
            ([], []),
            ([[1, None]], [[1, None]]),
            ([[1, 0]], [[1, 0]]),
            ([[1, None], [2, None]], [[1, None], [2, None]]),
            ([[5, 1], [6, None], [7, 0]], [[5, 1], [6, None], [7, 0]]),
            ([[0, None], [1, 0], [2, 1], [3, 2]], [[0, None], [1, 0], [2, 1], [3, 2]]),
            ([[1, None], [2, 2], [3, 2]], [[1, None], [2, 2], [3, 2]]),
            ([[42, None]], [[42, None]]),
            ([[1, 2], [2, None], [3, 0]], [[1, 2], [2, None], [3, 0]]),
            ([[1, None], [2, 0], [3, 1], [4, 2]], [[1, None], [2, 0], [3, 1], [4, 2]]),
        ],
    )
    def test_copy_random_list(
        self, nodes: list[list[int | None]], expected: list[list[int | None]]
    ):
        result = run_copy_random_list(Solution, nodes)
        assert_copy_random_list(result, expected)
