import pytest

from leetcode_py import logged_test

from .helpers import assert_min_deletion_size, run_min_deletion_size
from .solution import Solution


class TestDeleteColumnsToMakeSortedIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["babca", "bbazb"], 3),
            (["edcba"], 4),
            (["ghi", "def", "abc"], 0),
            (["a"], 0),
            (["ba"], 1),
            (["ab"], 0),
            (["aa", "aa"], 0),
            (["zyx", "wvu", "tsr"], 2),
            (["abc", "abc", "abc"], 0),
            (["cba", "abc"], 2),
            (["zz", "ab"], 0),
            (["cad", "bde", "acf"], 1),
            (["baab", "abab"], 2),
            (["abcd", "dcba"], 3),
            (["aabcc", "bbbbc", "bbcac", "baaba"], 2),
            (["acaa", "acaa", "bcbb", "caca"], 2),
            (["ac"], 0),
            (["cbbcc", "bccab", "babba"], 3),
            (["baca", "cacb"], 2),
            (["cbb", "cac"], 1),
            (["acba", "cbbb"], 3),
            (["acabb", "caaac"], 2),
            (["aa"], 0),
            (["c", "c", "b", "b"], 0),
        ],
    )
    def test_min_deletion_size(self, strs: list[str], expected: int):
        result = run_min_deletion_size(Solution, strs)
        assert_min_deletion_size(result, expected)
