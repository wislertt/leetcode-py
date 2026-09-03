import pytest

from leetcode_py import logged_test

from .helpers import assert_count_palindromic_subsequences, run_count_palindromic_subsequences
from .solution import Solution


class TestCountPalindromicSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("bccb", 6),
            ("a", 1),
            ("b", 1),
            ("aa", 2),
            ("ab", 2),
            ("aba", 4),
            ("abc", 3),
            ("aaaa", 4),
            ("abcd", 4),
            ("abcba", 10),
            ("abccba", 14),
            ("aabb", 4),
            ("abab", 6),
            ("abcdabcdabcd", 72),
            ("dcbadcba", 20),
            ("aaaabbbb", 8),
            ("abcdcba", 22),
            ("ddbbaacc", 8),
            ("acdbbccbda", 42),
            ("cacdbddc", 15),
            ("adadbcdbc", 17),
            ("adaccbbda", 25),
            ("bacbddada", 18),
            ("abdcdaccaba", 50),
            ("aaabdadacddc", 26),
            ("adcadccdba", 33),
            ("dcdabccbddad", 52),
            ("dbcabbcccc", 15),
            ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", 104860361),
            ("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd", 125826312),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 70),
            ("ababababababababababababababababababababababababababababababababababab", 78176334),
            ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcba", 562274879),
            ("bddbdcddbcbaabadbbcdadbdccdabbccbacbccbacdcdadcacbbcdcdbbdadcbbcccdb", 23767172),
            ("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd", 372554565),
        ],
    )
    def test_count_palindromic_subsequences(self, s: str, expected: int):
        result = run_count_palindromic_subsequences(Solution, s)
        assert_count_palindromic_subsequences(result, expected)
