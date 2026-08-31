import pytest

from leetcode_py import logged_test

from .helpers import assert_is_complete_tree, run_is_complete_tree
from .solution import Solution


class TestCheckCompletenessOfABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4, 5, 6], True),
            ([1, 2, 3, 4, 5, None, 7], False),
            ([1], True),
            ([1, 2], True),
            ([1, None, 2], False),
            ([1, 2, 3], True),
            ([1, 2, 3, 4], True),
            ([1, 2, 3, 4, None, None, 7], False),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([1, 2, 3, None, 4], False),
            ([1, 2, None, 4], False),
            ([1, 2, 3, 4, 5, None, None, 8], False),
            ([1, 2, 3, 4, 5, None, None, 8, 9], False),
        ],
    )
    def test_is_complete_tree(self, root_list: list[int | None], expected: bool):
        result = run_is_complete_tree(Solution, root_list)
        assert_is_complete_tree(result, expected)
