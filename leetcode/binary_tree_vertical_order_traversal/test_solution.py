import pytest

from leetcode_py import logged_test

from .helpers import assert_vertical_order, run_vertical_order
from .solution import Solution


class TestBinaryTreeVerticalOrderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
            ([3, 9, 8, 4, 0, 1, 7], [[4], [9], [3, 0, 1], [8], [7]]),
            (
                [1, 2, 3, 4, 10, 9, 11, None, 5, None, None, None, None, None, None, None, 6],
                [[4], [2, 5], [1, 10, 9, 6], [3], [11]],
            ),
            ([], []),
            ([1], [[1]]),
            ([1, 2, 3], [[2], [1], [3]]),
            ([1, 2, 3, 4, 5], [[4], [2], [1, 5], [3]]),
            ([1, 2, None, 3], [[3], [2], [1]]),
            ([1, None, 2, None, 3], [[1], [2], [3]]),
            ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
            ([1, 2, 3, 4, 5, 6, 7, 8], [[8], [4], [2], [1, 5, 6], [3], [7]]),
            ([5, 1, 6, None, 2, None, 7], [[1], [5, 2], [6], [7]]),
            ([-1, -2, -3], [[-2], [-1], [-3]]),
            ([1, 2, 3, None, None, 4, 5], [[2], [1, 4], [3], [5]]),
            ([4, 2, 6, 1, 3, 5, 7], [[1], [2], [4, 3, 5], [6], [7]]),
        ],
    )
    def test_vertical_order(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_vertical_order(Solution, root_list)
        assert_vertical_order(result, expected)
