import pytest

from leetcode_py import logged_test

from .helpers import assert_count_of_substrings, run_count_of_substrings
from .solution import Solution


class TestCountOfSubstringsContainingEveryVowelAndKConsonantsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word, k, expected",
        [
            ("aeioqq", 1, 0),
            ("aeiou", 0, 1),
            ("ieaouqqieaouqq", 1, 3),
            ("aeioubbb", 3, 1),
            ("aeioubcd", 2, 1),
            ("uoiea", 0, 1),
            ("aeiouaeiou", 0, 21),
            ("qaeiouq", 2, 1),
            ("aeiouxaeiou", 1, 21),
            ("bcdaeio", 1, 0),
            ("aeioub", 0, 1),
            ("aeioubb", 1, 1),
            ("coiieyocyay", 6, 0),
            ("ezefzeafx", 3, 0),
            ("xzuoddqeyu", 2, 0),
            ("uzfobfibauxa", 5, 0),
            ("zyiyeai", 1, 0),
            ("cuiod", 0, 0),
            ("zeiifexao", 4, 0),
            ("ieyzbd", 1, 0),
            ("ebabaague", 3, 0),
            ("xqyuc", 0, 0),
            ("uquaauuacgae", 6, 0),
            ("aiuubuy", 1, 0),
            ("xqdecioiebzy", 7, 0),
            ("aqooio", 0, 0),
        ],
    )
    def test_count_of_substrings(self, word: str, k: int, expected: int):
        result = run_count_of_substrings(Solution, word, k)
        assert_count_of_substrings(result, expected)
