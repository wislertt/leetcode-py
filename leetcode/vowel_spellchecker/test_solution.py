import pytest

from leetcode_py import logged_test

from .helpers import assert_spellchecker, run_spellchecker
from .solution import Solution


class TestVowelSpellchecker:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "wordlist, queries, expected",
        [
            (["KiTe", "kite", "hare", "Hare"], ["kite", "Kite"], ["kite", "KiTe"]),
            (["KiTe", "kite", "hare", "Hare"], ["KiTe", "Hare", "HARE"], ["KiTe", "Hare", "hare"]),
            (["KiTe", "kite", "hare", "Hare"], ["Hear", "hear"], ["", ""]),
            (["KiTe", "kite", "hare", "Hare"], ["keti", "keet", "keto"], ["KiTe", "", "KiTe"]),
            (["yellow"], ["YellOw"], ["yellow"]),
            (["YellOw"], ["yollow"], ["YellOw"]),
            (["YellOw"], ["yeellow"], [""]),
            (["YellOw"], ["yllw"], [""]),
            (["Yellow"], ["yellow"], ["Yellow"]),
            (["yellow"], ["yellow"], ["yellow"]),
            (["abc", "Abc"], ["ABC"], ["abc"]),
            (["man", "men"], ["mAn"], ["man"]),
            (["KiTe"], ["KETI"], ["KiTe"]),
            (["a"], ["A", "a", "e"], ["a", "a", "a"]),
            (["kgdb"], ["bkgua", "eusica", "bgs"], ["", "", ""]),
            (["gup", "bec"], ["ror", "bd", "kirb", "ru"], ["", "", "", ""]),
            (["kp", "ebekd", "iggpec"], ["db", "df", "biaai", "bdiud"], ["", "", "", ""]),
            (["uprs", "ko", "akdb"], ["ki", "oa"], ["ko", ""]),
        ],
    )
    def test_spellchecker(self, wordlist: list[str], queries: list[str], expected: list[str]):
        result = run_spellchecker(Solution, wordlist, queries)
        assert_spellchecker(result, expected)
