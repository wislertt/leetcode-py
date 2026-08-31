import pytest

from leetcode_py import logged_test

from .helpers import assert_count_characters, run_count_characters
from .solution import Solution


class TestFindWordsThatCanBeFormedByCharactersTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, chars, expected",
        [
            (["cat", "bt", "hat", "tree"], "atach", 6),
            (["hello", "world", "leetcode"], "welldonehoneyr", 10),
            (["a"], "a", 1),
            (["a"], "b", 0),
            (["ab", "ba"], "ab", 4),
            (["aaa"], "aa", 0),
            (["abc", "cba", "bca"], "abc", 9),
            (["z"], "zzzz", 1),
            (["letter", "letters"], "letters", 13),
            (["xyz"], "abc", 0),
            (["xy", "yxz", "zx"], "xyz", 7),
            (["xx", "xxx", "x"], "xx", 3),
            (["happy", "sad", "glad"], "happygladsad", 12),
            (["ab", "cd", "ef"], "abcdefgh", 6),
            (["ffff"], "fff", 0),
            (["spelling", "bee"], "spelbinge", 3),
        ],
    )
    def test_count_characters(self, words: list[str], chars: str, expected: int):
        result = run_count_characters(Solution, words, chars)
        assert_count_characters(result, expected)
