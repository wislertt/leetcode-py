import pytest

from leetcode_py import logged_test

from .helpers import assert_is_palindrome, run_is_palindrome
from .solution import Solution


class TestPalindromeLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([1, 2, 2, 1], True),
            ([1, 2], False),
            ([1], True),
            ([1, 1], True),
            ([1, 2, 1], True),
            ([1, 2, 3], False),
            ([1, 2, 3, 2, 1], True),
            ([1, 2, 3, 3, 2, 1], True),
            ([1, 2, 3, 4, 2, 1], False),
            ([0, 0], True),
            ([9], True),
            ([1, 2, 2, 2], False),
            ([1, 0, 0, 1], True),
            ([1, 2, 3, 4, 5, 6], False),
            ([2, 2, 2, 2], True),
            ([1, 2, 1, 2], False),
        ],
    )
    def test_is_palindrome(self, head_list: list[int], expected: bool):
        result = run_is_palindrome(Solution, head_list)
        assert_is_palindrome(result, expected)
