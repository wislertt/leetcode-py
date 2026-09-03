import pytest

from leetcode_py import logged_test

from .helpers import assert_distinct_subseq_ii, run_distinct_subseq_ii
from .solution import Solution


class TestDistinctSubsequencesII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abc", 7),
            ("aba", 6),
            ("aaa", 3),
            ("a", 1),
            ("b", 1),
            ("ab", 3),
            ("ba", 3),
            ("aa", 2),
            ("abab", 11),
            ("abba", 10),
            ("abcba", 26),
            ("abcabc", 51),
            ("aabbcc", 26),
            ("abababab", 87),
            ("abcdefgh", 255),
            ("aaaaaaaaaa", 10),
            ("abcdeabcdeabcde", 27727),
            ("zabcdefghijklmnopqrstuvwxy", 67108863),
            ("bacbacbacbacbac", 12639),
            ("ebgheafbebababdbehafbdffdbacfafadcabhggcebfdhachgchfgcaebhbc", 370069356),
            ("bbababbabbbabaaaaaaaabbbbabaabbbbbbaaabbaaaaabbaababbbbabbbaabbbaa", 337760141),
        ],
    )
    def test_distinct_subseq_ii(self, s: str, expected: int):
        result = run_distinct_subseq_ii(Solution, s)
        assert_distinct_subseq_ii(result, expected)
