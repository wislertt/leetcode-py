import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_find_all_concatenated_words_in_a_dict,
    run_find_all_concatenated_words_in_a_dict,
)
from .solution import Solution


class TestConcatenatedWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (
                [
                    "cat",
                    "cats",
                    "catsdogcats",
                    "dog",
                    "dogcatsdog",
                    "hippopotamuses",
                    "rat",
                    "ratcatdogcat",
                ],
                ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
            ),
            (["cat", "dog", "catdog"], ["catdog"]),
            (["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"]),
            (["a"], []),
            (["ab"], []),
            (["a", "b", "ab"], ["ab"]),
            (["a", "ab", "abc", "abcabc"], ["abcabc"]),
            (["x", "xx", "xxx", "xxxxx"], ["xx", "xxx", "xxxxx"]),
            (["me", "mo", "memo", "memome"], ["memo", "memome"]),
            (["to", "get", "her", "together"], ["together"]),
            (["dog", "cat", "dogcatcat"], ["dogcatcat"]),
            (["aa", "aaaa", "aaaaaa"], ["aaaa", "aaaaaa"]),
            (["a", "aa", "aaa"], ["aa", "aaa"]),
            (["hi", "hifi", "hifihifi"], ["hifihifi"]),
        ],
    )
    def test_find_all_concatenated_words_in_a_dict(self, words: list[str], expected: list[str]):
        result = run_find_all_concatenated_words_in_a_dict(Solution, words)
        assert_find_all_concatenated_words_in_a_dict(result, expected)
