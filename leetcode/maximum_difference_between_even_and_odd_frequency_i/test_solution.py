import pytest

from leetcode_py import logged_test

from .helpers import assert_max_difference, run_max_difference
from .solution import Solution


class TestMaximumDifferenceBetweenEvenAndOddFrequencyI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aaaaabbc", 3),
            ("abcabcab", 1),
            ("aabbb", 1),
            ("zzzyyxxx", 1),
            ("mmnnooopp", 1),
            ("aaabbccc", 1),
            ("abcc", -1),
            ("aabbcd", -1),
            ("aaaab", -3),
            ("aab", -1),
            ("abbcc", -1),
            ("qqqrss", 1),
            ("xxyyzzz", 1),
            ("eeeffggg", 1),
            ("tttuuuvvvv", -1),
            ("hhiiijjj", 1),
            ("abbaaababbabaabbbbbbb", 5),
            ("ceaeaaaebbbbedbecccedee", 3),
            ("cbabcbabacacabcaaa", -3),
            ("ccddacbdddbbdabacdbbaa", 3),
            ("abacabedceceac", 1),
            ("ddbcacbbbebdabcee", 1),
            ("abaaaabaa", 5),
            ("cbc", -1),
            ("abbcbacbcabccababcbab", 3),
            ("bbbabcbabacc", -3),
        ],
    )
    def test_max_difference(self, s: str, expected: int):
        result = run_max_difference(Solution, s)
        assert_max_difference(result, expected)
