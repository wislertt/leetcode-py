import pytest

from leetcode_py import logged_test

from .helpers import assert_make_equal, run_make_equal
from .solution import Solution


class TestRedistributeCharactersToMakeAllStringsEqual:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abc", "aabc", "bc"], True),
            (["ab", "a"], False),
            (["a"], True),
            (["a", "a"], True),
            (["a", "b"], False),
            (["ab", "ba"], True),
            (["abc", "def"], False),
            (["aa", "bb", "ab"], True),
            (["aaa", "aa"], False),
            (["abcabc", "cba"], False),
            (["zzzzz", "z"], True),
            (["zzzz", "zz", "zz"], False),
            (["dlie", "qzp", "px", "o", "vsyjg"], False),
            (["m", "rsq", "fbq", "h"], False),
            (["zysei", "eqh", "msmwuy", "lbs", "hht"], False),
            (["s", "lidod"], False),
            (["ohhsolrm", "hyuymw", "e", "tkze", "y"], False),
            (["c", "v", "l", "v"], False),
        ],
    )
    def test_make_equal(self, words: list[str], expected: bool):
        result = run_make_equal(Solution, words)
        assert_make_equal(result, expected)
