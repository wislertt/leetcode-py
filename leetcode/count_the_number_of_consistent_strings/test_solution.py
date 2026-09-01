import pytest

from leetcode_py import logged_test

from .helpers import assert_count_consistent_strings, run_count_consistent_strings
from .solution import Solution


class TestCountTheNumberOfConsistentStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "allowed, words, expected",
        [
            ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
            ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
            ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
            ("aqij", ["uuuu", "iaiji", "a", "aqqqjl"], 2),
            ("knetl", ["n", "n", "ekee"], 3),
            ("vy", ["y", "vvy", "vyyxyx", "yvyv"], 3),
            ("pe", ["ccpe", "lpel", "pppeex", "peeq", "ueu", "peped"], 0),
            ("t", ["tti"], 0),
            ("hazlj", ["haajz"], 1),
            ("wu", ["ouuo", "wud"], 0),
            ("eybgn", ["eye", "yge"], 2),
            ("qwula", ["ulquul", "qq"], 2),
            ("aocx", ["aoqaqo", "aocuao"], 0),
            ("eaq", ["a", "aqyae", "qaea", "qqeee"], 3),
            ("namj", ["na", "amm", "ymjymj", "dnmm"], 2),
            ("yiv", ["icycvy"], 0),
        ],
    )
    def test_count_consistent_strings(self, allowed: str, words: list[str], expected: int):
        result = run_count_consistent_strings(Solution, allowed, words)
        assert_count_consistent_strings(result, expected)
