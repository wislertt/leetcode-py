import pytest

from leetcode_py import logged_test

from .helpers import assert_num_special_equivalent_groups, run_num_special_equivalent_groups
from .solution import Solution


class TestGroupsOfSpecialEquivalentStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"], 3),
            (["abc", "acb", "bac", "bca", "cab", "cba"], 3),
            (["a"], 1),
            (["a", "b", "c"], 3),
            (["aa"], 1),
            (["aa", "aa"], 1),
            (["ab", "ba"], 2),
            (["ab", "ba", "ab"], 2),
            (["abc", "acb", "bac"], 3),
            (["abcd", "cdab"], 1),
            (["abcd", "badc"], 2),
            (["abcd", "dcba"], 2),
            (["abc", "cba", "bca", "cab"], 3),
            (["cadb", "abcd", "dcba"], 3),
            (["abcd", "cdab", "adcb", "cbad"], 1),
            (["gqqzllcgozovuyvwvoie", "gqqzllcgozovuyvwvoie", "qzigvloyuwvvczoegolq"], 1),
            (["hmbzqg", "alcmwn", "zgszpm", "xxerqt", "hgqzbm", "wncmal", "zgszpm"], 4),
            (["j", "r", "o", "j", "r", "o"], 3),
            (["na", "na", "na"], 1),
            (["gom", "btp", "jro", "rvz", "elt", "gom", "ptb", "orj", "zvr", "elt"], 5),
            (["mxcwi", "xckbr", "cwixm", "xckbr"], 2),
            (["ebdf", "emme", "wytv", "efdb", "meem", "tywv", "efdb"], 3),
            (["lg", "lc", "re", "lg", "lc", "re"], 3),
            (["curypp", "fmkkbo", "kjgvff", "usahhh", "pycpru", "bofkkm", "gjkvff"], 4),
            (["ru", "dz", "pg", "we", "fu", "pu", "ru", "dz", "pg", "we", "fu", "pu"], 6),
        ],
    )
    def test_num_special_equivalent_groups(self, words: list[str], expected: int):
        result = run_num_special_equivalent_groups(Solution, words)
        assert_num_special_equivalent_groups(result, expected)
