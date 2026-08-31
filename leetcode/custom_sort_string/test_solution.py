import pytest

from leetcode_py import logged_test

from .helpers import assert_custom_sort_string, run_custom_sort_string
from .solution import Solution


class TestCustomSortString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "order, s, expected",
        [
            ("cba", "abcd", "cbad"),
            ("bcafg", "abcd", "bcad"),
            ("world", "hello", "ollhe"),
            ("exv", "dttatvtterttxeree", "eeeexvdttatttrttr"),
            ("a", "aaaa", "aaaa"),
            ("a", "b", "b"),
            ("zyxwvu", "uutsrqponml", "uutsrqponml"),
            ("hgz", "ggghhzz", "hhgggzz"),
            ("k", "k", "k"),
            ("cba", "ccbbbaaaddd", "ccbbbaaaddd"),
            ("pqks", "spqqkkss", "pqqkksss"),
            ("mno", "onom", "mnoo"),
            ("abc", "abc", "abc"),
            ("cba", "aaa", "aaa"),
        ],
    )
    def test_custom_sort_string(self, order: str, s: str, expected: str):
        result = run_custom_sort_string(Solution, order, s)
        assert_custom_sort_string(result, expected)
