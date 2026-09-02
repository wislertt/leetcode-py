import pytest

from leetcode_py import logged_test

from .helpers import assert_is_sub_path, run_is_sub_path
from .solution import Solution


class TestLinkedListInBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, root_list, expected",
        [
            (
                [4, 2, 8],
                [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
                True,
            ),
            (
                [1, 4, 2, 6],
                [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
                True,
            ),
            (
                [1, 4, 2, 6, 8],
                [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
                False,
            ),
            ([1], [1], True),
            ([1], [2], False),
            ([7], [1, 7, 2], True),
            ([1, 2], [1, 2], True),
            ([2, 1], [1, 2], False),
            ([1, 2, 3], [1, None, 2, None, 3], True),
            ([1, 3], [1, None, 2, None, 3], False),
            ([5, 5, 5], [5, 5, None, 5], True),
            (
                [1, 4, 2, 6, 8],
                [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
                False,
            ),
            (
                [4, 2, 1],
                [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
                True,
            ),
            ([9, 9], [9, 9, 9], True),
            ([3], [5, 5], False),
            ([3, 5], [4, 5, 1, 5, 1], False),
            ([5, 4, 4], [2, 4], False),
            ([4, 1, 1], [2, 2], False),
            ([1, 3], [5, 1], False),
            ([5, 4, 2], [5, 4, 4, 4], False),
            ([2, 3], [1, 1, 2], False),
            ([3, 5, 5], [3, 4, 5, 4], False),
        ],
    )
    def test_is_sub_path(self, head_list: list[int], root_list: list[int | None], expected: bool):
        result = run_is_sub_path(Solution, head_list, root_list)
        assert_is_sub_path(result, expected)
