import pytest

from leetcode_py import logged_test

from .helpers import assert_bold_words, run_bold_words
from .solution import Solution


class TestBoldWordsInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, s, expected",
        [
            (["ab", "bc"], "aabcd", "a<b>abc</b>d"),
            (["ab", "cb"], "aabcd", "a<b>ab</b>cd"),
            ([], "hello", "hello"),
            (["a"], "a", "<b>a</b>"),
            (["b"], "a", "a"),
            (["aa", "b"], "aaabbb", "<b>aaabbb</b>"),
            (["abc"], "abcabcabc", "<b>abcabcabc</b>"),
            (["abc", "xyz"], "abcxyzuvw", "<b>abcxyz</b>uvw"),
            (["mis", "sis", "sip"], "mississippi", "<b>mississip</b>pi"),
            (["ab", "abcd"], "abcd", "<b>abcd</b>"),
            (["ap", "pl", "e"], "apple", "<b>apple</b>"),
            (["a", "b", "c"], "abc", "<b>abc</b>"),
            (["py", "pyt", "thon"], "pythonpython", "<b>pythonpython</b>"),
            (["leetcode"], "letmein", "letmein"),
            (["zz"], "zyzzzzy", "zy<b>zzzz</b>y"),
            (["xy", "yx"], "xyx", "<b>xyx</b>"),
        ],
    )
    def test_bold_words(self, words: list[str], s: str, expected: str):
        result = run_bold_words(Solution, words, s)
        assert_bold_words(result, expected)
