import pytest

from leetcode_py import logged_test

from .helpers import assert_is_even_odd_tree, run_is_even_odd_tree
from .solution import Solution


class TestEvenOddTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2], True),
            ([5, 4, 2, 3, 3, 7], False),
            ([5, 9, 1, 3, 5, 7], False),
            ([1], True),
            ([2], False),
            ([999998], False),
            ([1, 2], True),
            ([1, None, 4], True),
            ([1, 10], True),
            ([999999, 1000000], True),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 6], False),
            ([1, 10, 4, 3, 3, 7, 9], False),
            ([1, 4, 8, 3, 5, 7, 9], False),
            ([1, 8, 4, 7, 5, 9, 3], False),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, 2, None, None, 14, 13, 11, 9], False),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, 2], True),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, 2, None, None, 13, 15, 17, 19], True),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, 2, None, None, 15, 13, 11, 8], False),
            ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, 2, None, None, 13, 15, 11, 9], False),
        ],
    )
    def test_is_even_odd_tree(self, root_list: list[int | None], expected: bool):
        result = run_is_even_odd_tree(Solution, root_list)
        assert_is_even_odd_tree(result, expected)
