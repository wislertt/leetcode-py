import pytest

from leetcode_py import logged_test

from .helpers import assert_max_product, run_max_product
from .solution import Solution


class TestMaximumProductOfTheLengthOfTwoPalindromicSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("leetcodecom", 9),
            ("bb", 1),
            ("accbcaxxcxx", 25),
            ("ab", 1),
            ("aa", 1),
            ("abab", 4),
            ("aba", 2),
            ("aabb", 4),
            ("abcba", 6),
            ("abcd", 1),
            ("aabbccdd", 4),
            ("abaabcba", 15),
            ("acc", 2),
            ("abbaabbbabaa", 36),
            ("ceeeeedadeac", 30),
            ("eaeccdcd", 9),
            ("abbbbbaaaaab", 36),
            ("acccb", 3),
            ("aaaabbb", 12),
            ("aeebeeaabadc", 24),
        ],
    )
    def test_max_product(self, s: str, expected: int):
        result = run_max_product(Solution, s)
        assert_max_product(result, expected)
