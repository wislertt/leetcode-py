import pytest

from leetcode_py import logged_test

from .helpers import assert_score_of_string, run_score_of_string
from .solution import Solution


class TestScoreOfString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("hello", 13),
            ("zaz", 50),
            ("ab", 1),
            ("ba", 1),
            ("aa", 0),
            ("zz", 0),
            ("az", 25),
            ("za", 25),
            ("abc", 2),
            ("cba", 2),
            ("aaa", 0),
            ("abcdefghijklmnopqrstuvwxyz", 25),
            ("zyxwvutsrqponmlkjihgfedcba", 25),
            ("abcba", 4),
            ("leetcode", 63),
            ("aabbc", 2),
            ("abcabc", 6),
            ("aaaaabbbbb", 1),
            ("bababa", 5),
            ("xyzzyx", 4),
            ("cpgxigputxeoesemrhpglgcvgwcpibrl", 315),
            ("mfzgaqhuswkx", 121),
            ("oyjoz", 41),
            ("tfouviljlmktzlmtsugmpthxnldzvcwgcql", 272),
            ("wklasvshsnoiconspwxvmnxerbaengpo", 218),
            ("fzoftj", 64),
        ],
    )
    def test_score_of_string(self, s: str, expected: int):
        result = run_score_of_string(Solution, s)
        assert_score_of_string(result, expected)
