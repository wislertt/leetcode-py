import pytest

from leetcode_py import logged_test

from .helpers import assert_num_matching_subseq, run_num_matching_subseq
from .solution import Solution


class TestNumberOfMatchingSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, words, expected",
        [
            ("abcde", ["a", "bb", "acd", "ace"], 3),
            ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2),
            ("a", ["a", "a", "a"], 3),
            ("z", ["z"], 1),
            ("a", ["b", "c"], 0),
            ("abc", ["abc"], 1),
            ("abc", ["acb", "cab"], 0),
            ("aaa", ["aa", "aaa", "aaaa", "a"], 3),
            ("abppplee", ["able", "ale", "apple", "bale", "kangaroo"], 3),
            ("rabbbit", ["rabbit", "rabb", "bit", "bbt"], 4),
            ("abcde", ["edcba", "abcde", "aec", "ace"], 2),
            ("leetcode", ["leet", "code", "leetcode", "leeetcode", "coodde"], 3),
            ("xyxxy", ["xy", "yx", "xx", "yy", "xyx"], 5),
            ("mnmlmnm", ["mnm", "mml", "nnn", "lmn", "m"], 4),
            ("ccabcaaac", ["ca", "bb", "acc"], 2),
            ("bcabcb", ["cbc", "bcb", "aaabc"], 2),
            ("acbbba", ["c", "c", "bcaa", "bcb"], 2),
            ("cabac", ["cbaa", "ac"], 1),
            ("baaccbbbc", ["a", "ab", "bb"], 3),
            ("abbccaaaa", ["cca"], 1),
        ],
    )
    def test_num_matching_subseq(self, s: str, words: list[str], expected: int):
        result = run_num_matching_subseq(Solution, s, words)
        assert_num_matching_subseq(result, expected)
