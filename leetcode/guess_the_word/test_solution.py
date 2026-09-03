import pytest

from leetcode_py import logged_test

from .helpers import assert_find_secret_word, run_find_secret_word
from .solution import Solution


class TestGuessTheWord:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "secret, words, allowed_guesses, expected",
        [
            ("acckzz", ["acckzz", "ccbazz", "eiowzz", "abcczz"], 10, True),
            ("hamada", ["hamada", "khaled"], 10, True),
            ("aabbaa", ["aabbaa", "aabbab", "abbaaa", "baabaa", "aaaaab"], 10, True),
            ("zzzxxx", ["zzzxxx", "xxxyyy", "yyyzzz", "zxyxzy", "zxxyyz"], 10, True),
            ("monkey", ["monkey", "donkey", "moneyy", "honkey", "monies"], 30, True),
            ("banana", ["banana", "bandan", "banena", "nanaba", "ananab"], 15, True),
            ("zzzzzz", ["zzzzzz", "zzzzyz", "zzzyzz", "zzyzzz", "zyzzzz", "yzzzzz"], 10, True),
            ("status", ["status", "stains", "straps", "stairs", "starts"], 12, True),
            ("eaoeea", ["aouuie", "oiioee", "eaoeea", "ioooiu", "iuiaae", "oaoiuu"], 30, True),
            ("aaaabb", ["aaaabb", "bbbaab", "aaabab", "aabbba", "aaabaa", "aaaaba"], 28, True),
            ("oiiiau", ["eauiea", "eouuii", "oiiiau"], 13, True),
            ("dcedbb", ["eccbea", "cedbae", "dcedbb", "bcaadb", "bcdbbd"], 19, True),
            ("bbabbb", ["cbcada", "bbabbb"], 28, True),
            ("auoeeu", ["auoeeu", "iuieia"], 11, True),
            ("ddedec", ["cedgee", "eefcfg", "ccfggf", "ddedec"], 18, True),
            ("ecggdd", ["ggdgcg", "gecccf", "gdcggd", "ddddgc", "eegfcf", "ecggdd"], 25, True),
            ("baabba", ["bddaab", "dbaadc", "baabba", "bdaacc"], 14, True),
            ("dcdece", ["ecbeca", "bdeacb", "dcdece", "bcbbca", "becedc", "ebacba"], 23, True),
            ("dcbaaa", ["dcbaba", "aaebdc", "dcbaaa"], 28, True),
            ("ioaeio", ["uauaai", "ioaeio"], 24, True),
        ],
    )
    def test_find_secret_word(
        self, secret: str, words: list[str], allowed_guesses: int, expected: bool
    ):
        result = run_find_secret_word(Solution, secret, words, allowed_guesses)
        assert_find_secret_word(result, expected)
