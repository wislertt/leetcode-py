import pytest

from leetcode_py import logged_test

from .helpers import assert_preorder, run_preorder
from .solution import Solution


class TestNAryTreePreorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4]),
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
                [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
            ),
            ([], []),
            ([1], [1]),
            ([1, None, 2], [1, 2]),
            ([1, None, 2, 3], [1, 2, 3]),
            ([1, None, 2, None, 3, None, 4, None, 5], [1, 2, 3, 4, 5]),
            ([1, None, 3, 2, 4], [1, 3, 2, 4]),
            ([1, None, 2, 3, None, 4, 5, 6], [1, 2, 4, 5, 6, 3]),
            ([5, None, 4, None, 2, None, 3, 1], [5, 4, 2, 3, 1]),
            ([1, None, 10, 2, None, 20, 30, 40], [1, 10, 20, 30, 40, 2]),
            ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
            ([1, None, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1, None, 2, None, 3, 4, None, 5, None, 6], [1, 2, 3, 5, 4, 6]),
        ],
    )
    def test_preorder(self, root_list: list[int | None], expected: list[int]):
        result = run_preorder(Solution, root_list)
        assert_preorder(result, expected)
