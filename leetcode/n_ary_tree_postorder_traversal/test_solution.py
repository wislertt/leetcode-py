import pytest

from leetcode_py import logged_test

from .helpers import assert_postorder, run_postorder
from .solution import Solution


class TestNAryTreePostorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 3, 2, 4, None, 5, 6], [5, 6, 3, 2, 4, 1]),
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
                [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
            ),
            ([], []),
            ([1], [1]),
            ([1, None, 2], [2, 1]),
            ([1, None, 2, 3], [2, 3, 1]),
            ([1, None, 2, None, 3, None, 4, None, 5], [5, 4, 3, 2, 1]),
            ([1, None, 3, 2, 4], [3, 2, 4, 1]),
            ([1, None, 2, 3, None, 4, 5, 6], [4, 5, 6, 2, 3, 1]),
            ([5, None, 4, None, 2, None, 3, 1], [3, 1, 2, 4, 5]),
            ([1, None, 10, 2, None, 20, 30, 40], [20, 30, 40, 10, 2, 1]),
            ([1, None, 2, None, 3, None, 4], [4, 3, 2, 1]),
            ([1, None, 2, 3, 4, 5], [2, 3, 4, 5, 1]),
            ([1, None, 2, None, 3, 4, None, 5, None, 6], [5, 3, 6, 4, 2, 1]),
        ],
    )
    def test_postorder(self, root_list: list[int | None], expected: list[int]):
        result = run_postorder(Solution, root_list)
        assert_postorder(result, expected)
