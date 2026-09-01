import pytest

from leetcode_py import logged_test

from .helpers import assert_repeat_limited_string, run_repeat_limited_string
from .solution import Solution


class TestConstructStringWithRepeatLimit:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, repeat_limit, expected",
        [
            ("cczazcc", 3, "zzcccac"),
            ("aababab", 2, "bbabaa"),
            ("a", 1, "a"),
            ("aa", 1, "a"),
            ("aaa", 2, "aa"),
            ("aaa", 1, "a"),
            ("abc", 1, "cba"),
            ("aabbcc", 2, "ccbbaa"),
            ("zzzz", 4, "zzzz"),
            ("zzzz", 3, "zzz"),
            ("abcabc", 1, "cbcba"),
            ("aaabbbccc", 2, "ccbcbbaa"),
            ("banana", 2, "nnbaa"),
            ("abcde", 1, "edcba"),
            ("aabb", 1, "baba"),
            ("bbbbbbbbbb", 3, "bbb"),
            ("xyxyxyxy", 3, "yyyxyxxx"),
            ("aabbccddeeff", 1, "fefedcdcbaba"),
            ("zzzzaaaa", 2, "zzazzaa"),
            ("abcdefghijklmnop", 5, "ponmlkjihgfedcba"),
            ("ecdda", 3, "eddca"),
            ("eebdcad", 7, "eeddcba"),
            ("dbdbcabcba", 4, "ddccbbbbaa"),
            ("cddcbdca", 3, "dddcccba"),
            ("ebbceabeed", 4, "eeeedcbbba"),
            ("bcbd", 1, "dcb"),
            ("bdcbababdc", 10, "ddccbbbbaa"),
            ("debaeb", 4, "eedbba"),
            ("bcddbadecb", 5, "edddccbbba"),
            ("edbdccc", 2, "eddccbc"),
            ("bdbababebeee", 12, "eeeedbbbbbaa"),
            ("aacecdcc", 6, "edccccaa"),
            ("eeddbceead", 10, "eeeedddcba"),
            ("bcd", 2, "dcb"),
            ("bdbadeeabd", 7, "eedddbbbaa"),
            ("e", 1, "e"),
            ("c", 1, "c"),
            ("deaeaa", 3, "eedaaa"),
            ("edcdbcacaabc", 6, "eddccccbbaaa"),
            ("cd", 2, "dc"),
        ],
    )
    def test_repeat_limited_string(self, s: str, repeat_limit: int, expected: str):
        result = run_repeat_limited_string(Solution, s, repeat_limit)
        assert_repeat_limited_string(result, expected)
