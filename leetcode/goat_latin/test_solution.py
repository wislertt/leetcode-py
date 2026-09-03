import pytest

from leetcode_py import logged_test

from .helpers import assert_to_goat_latin, run_to_goat_latin
from .solution import Solution


class TestGoatLatin:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
            ("The quick brown fox", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa"),
            ("a", "amaa"),
            ("I", "Imaa"),
            ("apple", "applemaa"),
            ("goat", "oatgmaa"),
            ("UtAh", "UtAhmaa"),
            ("Orange", "Orangemaa"),
            ("egg", "eggmaa"),
            ("Under", "Undermaa"),
            ("each word turns", "eachmaa ordwmaaa urnstmaaaa"),
            ("a b c d", "amaa bmaaa cmaaaa dmaaaaa"),
            ("Zz Yy Xx", "zZmaa yYmaaa xXmaaaa"),
            ("The sky is blue", "heTmaa kysmaaa ismaaaa luebmaaaaa"),
            ("Quartz gem", "uartzQmaa emgmaaa"),
            ("wcjdS e", "cjdSwmaa emaaa"),
            ("oRfqX YlrqI", "oRfqXmaa lrqIYmaaa"),
            ("q zUA Y s", "qmaa UAzmaaa Ymaaaa smaaaaa"),
        ],
    )
    def test_to_goat_latin(self, sentence: str, expected: str):
        result = run_to_goat_latin(Solution, sentence)
        assert_to_goat_latin(result, expected)
