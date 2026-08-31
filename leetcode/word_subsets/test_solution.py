import pytest

from leetcode_py import logged_test

from .helpers import assert_word_subsets, run_word_subsets
from .solution import Solution


class TestWordSubsets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words1, words2, expected",
        [
            (
                ["amazon", "apple", "facebook", "google", "leetcode"],
                ["e", "o"],
                ["facebook", "google", "leetcode"],
            ),
            (
                ["amazon", "apple", "facebook", "google", "leetcode"],
                ["l", "o"],
                ["google", "leetcode"],
            ),
            (["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], ["c", "cc", "b"], ["cccbb"]),
            (["amazon"], ["amazon"], ["amazon"]),
            (["abc"], ["d"], []),
            (["a", "b", "c"], ["a", "b"], []),
            (["hello", "world"], ["lo", "rl"], ["world"]),
            (["aaaaa"], ["a", "aa", "aaa"], ["aaaaa"]),
            (["warrior", "world"], ["wrr"], ["warrior"]),
            (["leetcode", "online", "judge"], ["eo", "nt", "ok"], []),
            (["abcd", "dcba"], ["ab", "cd", "dc"], ["abcd", "dcba"]),
            (["xyz"], ["zz"], []),
        ],
    )
    def test_word_subsets(self, words1: list[str], words2: list[str], expected: list[str]):
        result = run_word_subsets(Solution, words1, words2)
        assert_word_subsets(result, expected)
