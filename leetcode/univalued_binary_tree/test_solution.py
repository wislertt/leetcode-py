import pytest

from leetcode_py import logged_test

from .helpers import assert_is_unival_tree, run_is_unival_tree
from .solution import Solution


class TestUnivaluedBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 1, 1, 1, 1, None, 1], True),
            ([2, 2, 2, 5, 2], False),
            ([1], True),
            ([0], True),
            ([1, 1], True),
            ([1, 2], False),
            ([99, 99], True),
            ([98, 99], False),
            ([0, 0, 0, 0, 0, 0, 0], True),
            ([1, 1, 1, 1, 1, 1, 1], True),
            ([1, 1, 1, None, 1, None, 1], True),
            ([1, 1, 1, None, 2], False),
            ([0, 0, 0, 1], False),
            ([9, 9, 9, 9, 9, 9, 10], False),
            ([1, 1, None, 1, None, 1, None, 1, None, 1], True),
            ([7, 7, None, 7, 7, None, 7, None, 7], True),
            ([57, 57, None, 57], True),
            ([88, 84, None, 49, None, 25], False),
            ([76, 76, None, 76, None, 76, None, 76, None, 76], True),
            ([45, 45, None, 45], True),
        ],
    )
    def test_is_unival_tree(self, root_list: list[int | None], expected: bool):
        result = run_is_unival_tree(Solution, root_list)
        assert_is_unival_tree(result, expected)
