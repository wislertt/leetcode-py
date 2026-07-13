import pytest

from leetcode_py import logged_test

from .helpers import assert_zigzag_level_order, run_zigzag_level_order
from .solution import Solution


class TestBinaryTreeZigzagLevelOrderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3], [[1], [3, 2]]),
            ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
            ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
            ([1, None, 2, None, 3], [[1], [2], [3]]),
            ([1, 2], [[1], [2]]),
            ([1, None, 2], [[1], [2]]),
            ([1, 2, 2, 3, 4, 4, 3], [[1], [2, 2], [3, 4, 4, 3]]),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]],
            ),
            ([3, 9, 20, None, None, 15, 7, 1, 2], [[3], [20, 9], [15, 7], [2, 1]]),
            (
                [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8],
                [[0], [4, 2], [1, 3, -1], [8, 6, 1, 5]],
            ),
        ],
    )
    def test_zigzag_level_order(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_zigzag_level_order(Solution, root_list)
        assert_zigzag_level_order(result, expected)
