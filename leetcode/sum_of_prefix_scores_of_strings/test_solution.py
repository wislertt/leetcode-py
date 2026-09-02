import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_prefix_scores, run_sum_prefix_scores
from .solution import Solution


class TestSumOfPrefixScoresOfStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abc", "ab", "bc", "b"], [5, 4, 3, 2]),
            (["abcd"], [4]),
            (["a"], [1]),
            (["a", "b", "c"], [1, 1, 1]),
            (["a", "ab", "abc"], [3, 5, 6]),
            (["ab", "a"], [3, 2]),
            (["aa", "aa"], [4, 4]),
            (["ab", "abc", "abcd"], [6, 8, 9]),
            (["ba", "ab"], [2, 2]),
            (["car", "card", "care"], [9, 10, 10]),
            (["leet", "leetcode", "leet"], [12, 16, 12]),
            (["abc", "abd", "abe"], [7, 7, 7]),
            (["abaa", "bcca", "ccbcb"], [4, 4, 5]),
            (["cbbb", "cb", "cbaab"], [8, 6, 9]),
            (["cacc"], [4]),
            (["ab", "cca", "ccbb"], [2, 5, 6]),
        ],
    )
    def test_sum_prefix_scores(self, words: list[str], expected: list[int]):
        result = run_sum_prefix_scores(Solution, words)
        assert_sum_prefix_scores(result, expected)
