import pytest

from leetcode_py import logged_test

from .helpers import assert_num_similar_groups, run_num_similar_groups
from .solution import Solution


class TestSimilarStringGroups:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["tars", "rats", "arts", "star"], 2),
            (["omv", "ovm"], 1),
            (["abc"], 1),
            (["a"], 1),
            (["aa", "aa"], 1),
            (["ab", "ba"], 1),
            (["abc", "acb", "bac"], 1),
            (["abcd", "abdc", "cdab"], 2),
            (["nice", "cnie", "ince"], 1),
            (["abcd", "abdc", "acbd"], 1),
            (["kccomw", "kwcomc", "womcck"], 2),
            (["ab", "ba", "ab"], 1),
            (["zz", "zz", "zz"], 1),
            (["ddgbe", "dedgb", "dedgb", "bgedd"], 3),
            (["fdged", "defgd", "dfgde", "fgedd", "egfdd"], 4),
            (["hcbdha", "bdahhc", "hbhcda", "bhchda", "bdhhca"], 5),
            (["fdedfh", "hdfdef", "fhfded", "ehfddf", "ddfefh", "ffhded"], 5),
            (["egge", "geeg", "egeg", "egge", "egeg", "eegg"], 1),
            (["feb", "efb", "bfe", "efb", "feb"], 1),
        ],
    )
    def test_num_similar_groups(self, strs: list[str], expected: int):
        result = run_num_similar_groups(Solution, strs)
        assert_num_similar_groups(result, expected)
