import pytest

from leetcode_py import logged_test

from .helpers import assert_make_good, run_make_good
from .solution import Solution


class TestMakeTheStringGreat:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("leEeetcode", "leetcode"),
            ("abBAcC", ""),
            ("s", "s"),
            ("Pp", ""),
            ("aA", ""),
            ("Aa", ""),
            ("ab", "ab"),
            ("aAbB", ""),
            ("RrLl", ""),
            ("McBfD", "McBfD"),
            ("hSbBmmOOoP", "hSmmOP"),
            ("qFxXfqqqQjjg", "qqqjjg"),
            ("mC", "mC"),
            ("kkkcAACc", "kkkcAA"),
            ("ZzYyXxWwVvUu", ""),
            ("SSKkaYP", "SSaYP"),
            ("DXpI", "DXpI"),
            ("BurwxLox", "BurwxLox"),
            ("WxivMPwhSLltjVa", "WxivMPwhStjVa"),
            ("PmTNYlSSQd", "PmTNYlSSQd"),
            ("vMuYO", "vMuYO"),
            ("nDkKSmdjYzWbGyzUbS", "nDSmdjYzWbGyzUbS"),
            ("FxrgexHxpuYE", "FxrgexHxpuYE"),
            ("fnsSsQjuZXeMXMFT", "fnsQjuZXeMXMFT"),
        ],
    )
    def test_make_good(self, s: str, expected: str):
        result = run_make_good(Solution, s)
        assert_make_good(result, expected)
