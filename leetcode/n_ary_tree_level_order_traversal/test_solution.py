import pytest

from leetcode_py import logged_test

from .helpers import assert_level_order, run_level_order
from .solution import Solution


class TestNAryTreeLevelOrderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]]),
            (
                [
                    1,
                    None,
                    2,
                    3,
                    4,
                    5,
                    None,
                    None,
                    6,
                    7,
                    None,
                    8,
                    None,
                    9,
                    10,
                    None,
                    None,
                    11,
                    None,
                    12,
                    None,
                    13,
                    None,
                    None,
                    14,
                ],
                [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
            ),
            ([], []),
            ([1], [[1]]),
            ([1, None, 2], [[1], [2]]),
            ([1, None, 2, 3], [[1], [2, 3]]),
            ([1, None, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
            ([1, None, 3, 2, 4], [[1], [3, 2, 4]]),
            ([1, None, 2, 3, None, 4, 5, 6], [[1], [2, 3], [4, 5, 6]]),
            ([5, None, 4, None, 2, None, 3, 1], [[5], [4], [2], [3, 1]]),
            ([1, None, 10, 2, None, 20, 30, 40], [[1], [10, 2], [20, 30, 40]]),
            ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]]),
            ([1, None, 2, 3, 4, 5], [[1], [2, 3, 4, 5]]),
            ([1, None, 2, None, 3, 4, None, 5, None, 6], [[1], [2], [3, 4], [5, 6]]),
            ([1, None, 2, 3, 4, None, None, None, 5, 6, None, 7], [[1], [2, 3, 4], [5, 6], [7]]),
            ([1, None, 2, 3, None, 4, None, None, 5, 6, None, 7], [[1], [2, 3], [4], [5, 6], [7]]),
        ],
    )
    def test_level_order(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_level_order(Solution, root_list)
        assert_level_order(result, expected)
