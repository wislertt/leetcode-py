import pytest

from leetcode_py import logged_test

from .helpers import assert_add_bold_tag, run_add_bold_tag
from .solution import Solution


class TestAddBoldTagInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, words, expected",
        [
            ("abcxyz123", ["abc", "123"], "<b>abc</b>xyz<b>123</b>"),
            ("aaabbb", ["aa", "b"], "<b>aaabbb</b>"),
            ("abcxyz123", ["abc", "xyz", "123"], "<b>abcxyz123</b>"),
            ("aaabbbaaa", ["aaa"], "<b>aaa</b>bbb<b>aaa</b>"),
            ("abcdefg", ["xyz"], "abcdefg"),
            ("abcdefg", [], "abcdefg"),
            ("a", ["a"], "<b>a</b>"),
            ("a", ["b"], "a"),
            ("aaaa", ["a"], "<b>aaaa</b>"),
            ("abcd", ["ab", "cd"], "<b>abcd</b>"),
            ("abcabcabc", ["bc"], "a<b>bc</b>a<b>bc</b>a<b>bc</b>"),
            ("x10x", ["1", "0"], "x<b>10</b>x"),
            ("mississippi", ["mis", "sis", "sip"], "<b>mississip</b>pi"),
        ],
    )
    def test_add_bold_tag(self, s: str, words: list[str], expected: str):
        result = run_add_bold_tag(Solution, s, words)
        assert_add_bold_tag(result, expected)
