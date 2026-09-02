import pytest

from leetcode_py import logged_test

from .helpers import assert_evaluate_tree, run_evaluate_tree
from .solution import Solution


class TestEvaluateBooleanBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 1, 3, None, None, 0, 1], True),
            ([0], False),
            ([1], True),
            ([2, 0, 1], True),
            ([3, 0, 1], False),
            ([3, 1, 1], True),
            ([2, 0, 0], False),
            ([2, 3, 2, 1, 1, 0, 1], True),
            ([3, 2, 3, 0, 1, 1, 0], False),
            ([3, 1, 0], False),
            ([2, 1, 0], True),
            ([3, 3, 3, 0, 0, 0, 0], False),
            ([2, 3, 2, 0, 1, 0, 1], True),
            ([3, 2, 2, 1, 1, 1, 0], True),
            ([3, 2, 3, 1, 1, 1, 0], False),
            ([2, 2, 2, 1, 0, 1, 0], True),
            ([2, 2, 3, 1, 1, 1, 0], True),
            ([2, 3, 3, 2, 3, 3, 3, 0, 1, 1, 1, 0, 0, 1, 0], True),
            ([3, 3, 3, 2, 3, 2, 2, 0, 0, 1, 1, 1, 0, 0, 1], False),
            ([3, 2, 2, 2, 3, 2, 2, 0, 1, 0, 1, 0, 0, 0, 1], True),
            ([2, 3, 2, 2, 2, 3, 2, 1, 1, 0, 1, 1, 0, 1, 1], True),
        ],
    )
    def test_evaluate_tree(self, root_list: list[int | None], expected: bool):
        result = run_evaluate_tree(Solution, root_list)
        assert_evaluate_tree(result, expected)
