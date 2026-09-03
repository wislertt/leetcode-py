import pytest

from leetcode_py import logged_test

from .helpers import assert_k_similarity, run_k_similarity
from .solution import Solution


class TestTestKSimilarStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("ab", "ba", 1),
            ("abc", "bca", 2),
            ("a", "a", 0),
            ("abcd", "abcd", 0),
            ("abcdef", "abcdef", 0),
            ("abab", "baba", 2),
            ("aabb", "bbaa", 2),
            ("aabbcc", "ccbbaa", 2),
            ("abcdabcd", "dcbadcba", 4),
            ("abcabc", "cbacba", 2),
            ("aabbc", "cbaba", 2),
            ("cdacbaccac", "abcacdccca", 5),
            ("dabba", "badba", 1),
            ("bbcddabbd", "acbbbddbd", 4),
            ("bccacddb", "bccdacbd", 3),
            ("cacdb", "cdacb", 2),
            ("adabccb", "aabcbdc", 4),
            ("ddcabdcac", "cccddabad", 4),
            ("cdcadccbbcb", "abbcdbccccd", 4),
            ("bdbcac", "cbcdab", 3),
        ],
    )
    def test_k_similarity(self, s1: str, s2: str, expected: int):
        result = run_k_similarity(Solution, s1, s2)
        assert_k_similarity(result, expected)
