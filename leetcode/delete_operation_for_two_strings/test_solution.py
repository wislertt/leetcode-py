import pytest

from leetcode_py import logged_test

from .helpers import assert_min_distance, run_min_distance
from .solution import Solution


class TestDeleteOperationForTwoStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            ("sea", "eat", 2),
            ("leetcode", "etco", 4),
            ("a", "a", 0),
            ("a", "b", 2),
            ("ab", "ab", 0),
            ("ab", "ba", 2),
            ("abc", "abc", 0),
            ("abc", "def", 6),
            ("abcde", "ace", 2),
            ("horse", "ros", 4),
            ("abcdef", "azced", 5),
            ("intention", "execution", 8),
            ("xy", "x", 1),
            ("aa", "aaa", 1),
            ("abcabc", "bcbcca", 4),
            ("mississippi", "ssippi", 5),
            ("acbcb", "cdcbab", 5),
            ("babbdd", "bcadda", 4),
            ("bd", "cadd", 4),
            ("c", "bdddd", 6),
        ],
    )
    def test_min_distance(self, word1: str, word2: str, expected: int):
        result = run_min_distance(Solution, word1, word2)
        assert_min_distance(result, expected)
