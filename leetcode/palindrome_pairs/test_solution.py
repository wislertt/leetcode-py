import pytest

from leetcode_py import logged_test

from .helpers import assert_palindrome_pairs, run_palindrome_pairs
from .solution import Solution


class TestPalindromePairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
            (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
            (["a", ""], [[0, 1], [1, 0]]),
            (["a", "b", "c"], []),
            (["abc", ""], []),
            (["ab", "ba"], [[0, 1], [1, 0]]),
            (["ab", ""], []),
            (["aba", ""], [[0, 1], [1, 0]]),
            (["lls", "s"], [[1, 0]]),
            (["abba", ""], [[0, 1], [1, 0]]),
            (["abc", "ab"], []),
            (["abc", "cba"], [[0, 1], [1, 0]]),
            (["ab", "ba", "cd", "dc"], [[0, 1], [1, 0], [2, 3], [3, 2]]),
            (["abcd", "dcba", "xyz", "zyx"], [[0, 1], [1, 0], [2, 3], [3, 2]]),
            (["ab", "cba"], [[0, 1]]),
        ],
    )
    def test_palindrome_pairs(self, words: list[str], expected: list[list[int]]):
        result = run_palindrome_pairs(Solution, words)
        assert_palindrome_pairs(result, expected)
