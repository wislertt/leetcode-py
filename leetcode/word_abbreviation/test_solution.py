import pytest

from leetcode_py import logged_test

from .helpers import assert_words_abbreviation, run_words_abbreviation
from .solution import Solution


class TestWordAbbreviation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (
                [
                    "like",
                    "god",
                    "internal",
                    "me",
                    "internet",
                    "interval",
                    "intension",
                    "face",
                    "intrusion",
                ],
                ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"],
            ),
            (["aa", "aaa"], ["aa", "aaa"]),
            (["abcdef", "abndef"], ["abc2f", "abn2f"]),
            (["international"], ["i11l"]),
            (["ab"], ["ab"]),
            (["abc", "abd"], ["abc", "abd"]),
            (["kanariozelo", "narciso", "kanario", "narcisos"], ["k9o", "n5o", "k5o", "n6s"]),
            (["god", "geed"], ["god", "g2d"]),
            (["cd", "ef"], ["cd", "ef"]),
            (["my", "mine", "mule", "mice"], ["my", "mine", "mule", "mice"]),
            (["mule", "mine", "my", "mice"], ["mule", "mine", "my", "mice"]),
            (["ebcede", "ea", "cebbd"], ["e4e", "ea", "c3d"]),
            (
                ["ddbbbe", "aabea", "acde", "ddedb", "aabd", "cdc"],
                ["d4e", "a3a", "a2e", "d3b", "a2d", "cdc"],
            ),
            (["deceed", "bcaceb", "eeea", "ecc", "ad"], ["d4d", "b4b", "e2a", "ecc", "ad"]),
            (["ca", "bacdd", "ae", "adecec", "bacaaa"], ["ca", "b3d", "ae", "a4c", "b4a"]),
        ],
    )
    def test_words_abbreviation(self, words: list[str], expected: list[str]):
        result = run_words_abbreviation(Solution, words)
        assert_words_abbreviation(result, expected)
