import pytest

from leetcode_py import logged_test

from .helpers import assert_prefix_count, run_prefix_count
from .solution import Solution


class TestCountingWordsWithAGivenPrefix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, pref, expected",
        [
            (["pay", "attention", "practice", "attend"], "at", 2),
            (["leetcode", "win", "loops", "success"], "code", 0),
            (["at", "at", "at"], "at", 3),
            (["a", "b", "c"], "a", 1),
            (["a", "b", "c"], "z", 0),
            (["attend"], "attend", 1),
            (["attend"], "attention", 0),
            (["apple", "apply", "app", "apt"], "app", 3),
            (["prefix", "preform", "prevent", "pretend"], "pre", 4),
            (["misjudge", "mislead", "mistake", "mission"], "mis", 4),
            (["unbelievable", "unclear", "unfit", "unjust"], "un", 4),
            (["word", "words", "wording", "wordy"], "wordy", 1),
            (["aa", "ab", "ba"], "aa", 1),
            (["hello", "hel", "hell", "helicopter"], "hell", 2),
            (["neetcode", "neet", "code", "leet"], "neet", 2),
        ],
    )
    def test_prefix_count(self, words: list[str], pref: str, expected: int):
        result = run_prefix_count(Solution, words, pref)
        assert_prefix_count(result, expected)
