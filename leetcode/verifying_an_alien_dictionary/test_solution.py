import pytest

from leetcode_py import logged_test

from .helpers import assert_is_alien_sorted, run_is_alien_sorted
from .solution import Solution


class TestVerifyingAnAlienDictionary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, order, expected",
        [
            (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
            (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
            (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
            (["a"], "abcdefghijklmnopqrstuvwxyz", True),
            (["a", "a"], "abcdefghijklmnopqrstuvwxyz", True),
            (["a", "b"], "abcdefghijklmnopqrstuvwxyz", True),
            (["b", "a"], "abcdefghijklmnopqrstuvwxyz", False),
            (["app", "apple"], "abcdefghijklmnopqrstuvwxyz", True),
            (["abc", "abc"], "abcdefghijklmnopqrstuvwxyz", True),
            (["zebra", "apple"], "zyxwvutsrqponmlkjihgfedcba", True),
            (["apple", "zebra"], "zyxwvutsrqponmlkjihgfedcba", False),
            (["ab", "ac", "ad"], "abcdefghijklmnopqrstuvwxyz", True),
            (["ad", "ac", "ab"], "zyxwvutsrqponmlkjihgfedcba", True),
            (["hello", "hello"], "zyxwvutsrqponmlkjihgfedcba", True),
            (["cat", "car"], "abcdefghijklmnopqrstuvwxyz", False),
            (["car", "cat"], "abcdefghijklmnopqrstuvwxyz", True),
            (["aa", "ab", "ba", "bb"], "abcdefghijklmnopqrstuvwxyz", True),
            (["bb", "ba"], "abcdefghijklmnopqrstuvwxyz", False),
        ],
    )
    def test_is_alien_sorted(self, words: list[str], order: str, expected: bool):
        result = run_is_alien_sorted(Solution, words, order)
        assert_is_alien_sorted(result, expected)
