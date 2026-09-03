import pytest

from leetcode_py import logged_test

from .helpers import assert_check_equal_tree, run_check_equal_tree
from .solution import Solution


class TestEqualTreePartition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([5, 10, 10, None, None, 2, 3], True),
            ([1, 2, 10, None, None, 2, 20], False),
            ([0], False),
            ([1], False),
            ([-1], False),
            ([0, 0], True),
            ([1, 1], True),
            ([-1, -1], True),
            ([2, 1, 1], False),
            ([4, 2, 6, 1, 3, 5, 7], False),
            ([1, 7, 3, 1, 2], False),
            ([0, 0, 0], True),
            ([0, 1, -1], False),
            ([1, 2, None, 3, None, 4], False),
            ([100000, 100000], True),
            ([-100000, -100000], True),
            ([1, 2, 3, 4, None, None, 5, 6], False),
            ([3, 1, 2, None, None, None, 1], False),
            ([1, -3, 0, 3, -3, 1, 2], False),
            ([-3, 2], False),
            ([-3, 0, -2, 2, 3, None, 0], True),
            ([2, 1, 2], False),
            ([-3, -2, 1, -3], False),
            ([0, 0, 1, None, None, -2, 1], True),
            ([3, -1, 2], True),
            ([3, 2, 0], False),
        ],
    )
    def test_check_equal_tree(self, root_list: list[int | None], expected: bool):
        result = run_check_equal_tree(Solution, root_list)
        assert_check_equal_tree(result, expected)
