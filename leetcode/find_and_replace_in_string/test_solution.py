import pytest

from leetcode_py import logged_test

from .helpers import assert_find_replace_string, run_find_replace_string
from .solution import Solution


class TestFindAndReplaceInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, indices, sources, targets, expected",
        [
            ("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"], "eeebffff"),
            ("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"], "eeecd"),
            ("abcd", [0], ["ab"], ["eee"], "eeecd"),
            ("abcd", [3], ["d"], ["z"], "abcz"),
            ("abcd", [3], ["de"], ["z"], "abcd"),
            ("abcde", [0, 2], ["ab", "cd"], ["x", "y"], "xye"),
            ("vmvvggive", [5, 0], ["g", "vmvv"], ["h", "i"], "ighive"),
            ("abcdef", [1, 3], ["bc", "de"], ["bc", "def"], "abcdeff"),
            ("a", [0], ["a"], ["aa"], "aa"),
            ("hello", [0, 4], ["he", "lo"], ["hey", "lo!"], "heyllo"),
            ("cggfgfbe", [2], ["gf"], ["a"], "cgagfbe"),
            ("dagdcbacf", [7, 4], ["c", "cb"], ["dfg", "chb"], "dagdchbadfgf"),
            ("dbhhbfab", [1, 3, 4], ["bh", "h", "bf"], ["b", "baaf", "ehgf"], "dbbaafehgfab"),
            ("cdeef", [4, 1, 3], ["cdd", "de", "db"], ["acf", "e", "ce"], "ceef"),
            ("bghfh", [2, 1], ["hf", "g"], ["fa", "aheg"], "bahegfah"),
            ("afabhggc", [4, 1], ["hg", "f"], ["ch", "bd"], "abdabchgc"),
        ],
    )
    def test_find_replace_string(
        self, s: str, indices: list[int], sources: list[str], targets: list[str], expected: str
    ):
        result = run_find_replace_string(Solution, s, indices, sources, targets)
        assert_find_replace_string(result, expected)
