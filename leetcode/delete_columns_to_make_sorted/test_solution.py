import pytest

from leetcode_py import logged_test

from .helpers import assert_min_deletion_size, run_min_deletion_size
from .solution import Solution


class TestDeleteColumnsToMakeSorted:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["cba", "daf", "ghi"], 1),
            (["a", "b"], 0),
            (["zyx", "wvu", "tsr"], 3),
            (["abc", "bce", "cae"], 1),
            (["a"], 0),
            (["z"], 0),
            (["ab", "cd"], 0),
            (["ba", "cd"], 0),
            (["ba", "ab"], 1),
            (["abc"], 0),
            (["aaa", "aaa"], 0),
            (["az", "za"], 1),
            (["az", "za", "az"], 2),
            (["xyz", "abc"], 3),
            (["c", "c", "b"], 1),
            (["b", "c", "c"], 0),
            (["abbaabacca"], 0),
            (["aaba", "bcbb"], 0),
            (["cacc", "abab", "bcbc", "ccca"], 3),
            (["abaccbac", "bbbbbcab"], 3),
            (["bbccc", "cbbbc"], 2),
            (["caacb", "bcbac", "acbaa"], 3),
            (["aaaaabbababbbaaaabba", "baabbbabbaabbabaabab", "aababbaabbaabbbbbbbb"], 7),
            (["babbaabaaa", "bbbbbbaabb", "aabbababaa", "bbabbaaaaa", "bbbaababaa"], 10),
        ],
    )
    def test_min_deletion_size(self, strs: list[str], expected: int):
        result = run_min_deletion_size(Solution, strs)
        assert_min_deletion_size(result, expected)
