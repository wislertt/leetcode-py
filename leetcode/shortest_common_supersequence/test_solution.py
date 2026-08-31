import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_common_supersequence, run_shortest_common_supersequence
from .solution import Solution


class TestShortestCommonSupersequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "str1, str2, expected_length",
        [
            ("abac", "cab", 5),
            ("aaaaaaaa", "aaaaaaaa", 8),
            ("abc", "abc", 3),
            ("abc", "def", 6),
            ("a", "a", 1),
            ("a", "b", 2),
            ("ab", "ba", 3),
            ("geek", "eke", 5),
            ("AGGTAB", "GXTXAYB", 9),
            ("aaaa", "aa", 4),
            ("bcaeacdea", "afabacf", 13),
            ("xyxyx", "yxyxy", 6),
            ("kjklk", "kkjkk", 6),
            ("abababab", "babababa", 9),
        ],
    )
    def test_shortest_common_supersequence(self, str1: str, str2: str, expected_length: int):
        result = run_shortest_common_supersequence(Solution, str1, str2)
        assert_shortest_common_supersequence(result, str1, str2, expected_length)
