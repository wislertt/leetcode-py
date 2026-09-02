import pytest

from leetcode_py import logged_test

from .helpers import assert_clone_tree, run_clone_tree
from .solution import Solution


class TestCloneNAryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 3, 2, 4, None, 5, 6], [1, None, 3, 2, 4, None, 5, 6]),
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
            ),
            ([], []),
            ([1], [1]),
            ([1, None, 2], [1, None, 2]),
            ([1, None, 2, 3], [1, None, 2, 3]),
            ([1, None, 2, None, 3, None, 4, None, 5], [1, None, 2, None, 3, None, 4, None, 5]),
            ([1, None, 3, 2, 4], [1, None, 3, 2, 4]),
            ([1, None, 2, 3, None, 4, 5, 6], [1, None, 2, 3, None, 4, 5, 6]),
            ([5, None, 4, None, 2, None, 3, 1], [5, None, 4, None, 2, None, 3, 1]),
            ([1, None, 10, 2, None, 20, 30, 40], [1, None, 10, 2, None, 20, 30, 40]),
            ([1, None, 2, 3, 4, 5], [1, None, 2, 3, 4, 5]),
            (
                [1, None, 2, None, 3, 4, None, 5, None, 6],
                [1, None, 2, None, 3, 4, None, 5, None, 6],
            ),
            (
                [4, None, 1, None, 2, None, 3, None, 7, 8, 9],
                [4, None, 1, None, 2, None, 3, None, 7, 8, 9],
            ),
            ([7, None, 3, None, 9, 1, 2, None, 5, 6], [7, None, 3, None, 9, 1, 2, None, 5, 6]),
            (
                [1, None, 2, 3, 5, 8, None, 9, None, 4, 7, None, 6],
                [1, None, 2, 3, 5, 8, None, 9, None, 4, 7, None, 6],
            ),
            (
                [1, None, 2, 5, 7, None, 3, 4, None, 8, None, None, 6],
                [1, None, 2, 5, 7, None, 3, 4, None, 8, None, None, 6],
            ),
            ([1, None, 2, 3, None, None, 4], [1, None, 2, 3, None, None, 4]),
            ([1, None, 2, None, 3, 4, 5], [1, None, 2, None, 3, 4, 5]),
            ([1, None, 2, 5, None, 3, 4, 6], [1, None, 2, 5, None, 3, 4, 6]),
            (
                [1, None, 2, 5, None, 3, None, None, 4, 6, None, None, 7, 8],
                [1, None, 2, 5, None, 3, None, None, 4, 6, None, None, 7, 8],
            ),
        ],
    )
    def test_clone_tree(self, root_list: list[int | None], expected: list[int | None]):
        result = run_clone_tree(Solution, root_list)
        assert_clone_tree(result, expected)
