import pytest

from leetcode_py import logged_test

from .helpers import assert_common_chars, run_common_chars
from .solution import Solution


class TestFindCommonCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["bella", "label", "roller"], ["e", "l", "l"]),
            (["cool", "lock", "cook"], ["c", "o"]),
            (["a"], ["a"]),
            (["a", "a", "a"], ["a"]),
            (["ab"], ["a", "b"]),
            (["ab", "cd"], []),
            (["abc", "bca", "cab"], ["a", "b", "c"]),
            (["hello", "world"], ["l", "o"]),
            (["aaaa", "aa", "aaa"], ["a", "a"]),
            (["xyz"], ["x", "y", "z"]),
            (["abcde", "edcba", "cdeba"], ["a", "b", "c", "d", "e"]),
            (["fast", "safe", "soft"], ["f", "s"]),
        ],
    )
    def test_common_chars(self, words: list[str], expected: list[str]):
        result = run_common_chars(Solution, words)
        assert_common_chars(result, expected)
