import pytest

from leetcode_py import logged_test

from .helpers import assert_min_deletion_size, run_min_deletion_size
from .solution import Solution


class TestDeleteColumnsToMakeSortedII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["ca", "bb", "ac"], 1),
            (["xc", "yb", "za"], 0),
            (["zyx", "wvu", "tsr"], 3),
            (["a"], 0),
            (["z"], 0),
            (["abc"], 0),
            (["a", "b", "c"], 0),
            (["cba", "abc"], 1),
            (["aa", "aa"], 0),
            (["ba", "ab"], 1),
            (["zy", "yx"], 2),
            (["abc", "abd"], 0),
            (["az", "za", "az"], 2),
            (["ab", "ba", "ab"], 2),
            (["cedb", "edca", "edaa", "becc"], 4),
            (["deccd", "eeace", "bceaa"], 5),
            (["c", "c", "c", "a"], 1),
            (["bac"], 0),
            (["bedcb", "dbdcc", "cacab"], 5),
            (["b"], 0),
            (["eabab", "ccced", "bdacb", "aaecb"], 5),
            (["daadde", "cdabcc", "bbcbcc"], 5),
            (["abd", "baa", "acc", "bed", "dbe"], 3),
            (["eeed", "acaa", "dade", "dbcc", "abde"], 4),
        ],
    )
    def test_min_deletion_size(self, strs: list[str], expected: int):
        result = run_min_deletion_size(Solution, strs)
        assert_min_deletion_size(result, expected)
