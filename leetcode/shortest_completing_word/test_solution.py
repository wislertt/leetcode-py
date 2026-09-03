import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_completing_word, run_shortest_completing_word
from .solution import Solution


class TestShortestCompletingWord:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "license_plate, words, expected",
        [
            ("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),
            ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
            ("aBc 12c", ["abccdef", "caaacab", "cbca"], "cbca"),
            ("3A", ["b", "a", "ca"], "a"),
            ("A", ["banana", "apple"], "apple"),
            ("Pp", ["p", "apple", "pp"], "pp"),
            ("AbC", ["cba", "abc"], "cba"),
            ("0W", ["ww", "www"], "ww"),
            ("Ss", ["s", "sa", "ssss"], "ssss"),
            ("Zz", ["aaz", "zzq"], "zzq"),
            ("1Q2", ["queue", "quit", "quick"], "quit"),
            ("B", ["a", "bb", "b"], "b"),
            ("9l7", ["hello", "world", "level"], "hello"),
            ("W1n", ["now", "win", "own"], "now"),
            ("Gg", ["gag", "egg", "gig"], "gag"),
            ("xY", ["xylophone", "yax"], "yax"),
            ("1M2", ["mum", "mom"], "mum"),
        ],
    )
    def test_shortest_completing_word(self, license_plate: str, words: list[str], expected: str):
        result = run_shortest_completing_word(Solution, license_plate, words)
        assert_shortest_completing_word(result, expected)
