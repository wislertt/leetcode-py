import pytest

from leetcode_py import logged_test

from .helpers import assert_uncommon_from_sentences, run_uncommon_from_sentences
from .solution import Solution


class TestUncommonWordsFromTwoSentences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
            ("apple apple", "banana", ["banana"]),
            ("a", "b", ["a", "b"]),
            ("a", "a", []),
            ("a b c", "a b c", []),
            ("a b c d", "b c d e", ["a", "e"]),
            ("apple", "apple apple", []),
            ("a b", "c d", ["a", "b", "c", "d"]),
            ("x y z w", "z w q r", ["q", "r", "x", "y"]),
            ("aa aa", "aa", []),
            ("ab bc ca", "bc ab", ["ca"]),
            ("one two", "three four five", ["five", "four", "one", "three", "two"]),
            ("hello world hello", "world", []),
            ("p q", "p q p q", []),
        ],
    )
    def test_uncommon_from_sentences(self, s1: str, s2: str, expected: list[str]):
        result = run_uncommon_from_sentences(Solution, s1, s2)
        assert_uncommon_from_sentences(result, expected)
