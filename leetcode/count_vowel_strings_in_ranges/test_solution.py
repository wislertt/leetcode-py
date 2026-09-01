import pytest

from leetcode_py import logged_test

from .helpers import assert_vowel_strings, run_vowel_strings
from .solution import Solution


class TestCountVowelStringsInRanges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, queries, expected",
        [
            (["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]], [2, 3, 0]),
            (["a", "e", "i"], [[0, 2], [0, 1], [2, 2]], [3, 2, 1]),
            (["aba"], [[0, 0]], [1]),
            (["xyz"], [[0, 0]], [0]),
            (["aa", "bb", "ee", "cc", "oo"], [[0, 4], [0, 0], [4, 4], [2, 3]], [3, 1, 1, 1]),
            (["bcd", "fgh", "jkl"], [[0, 2], [1, 2], [0, 0]], [0, 0, 0]),
            (["a", "b", "e", "c", "i", "x"], [[0, 5], [1, 3], [2, 2]], [3, 1, 1]),
            (["uo", "ou", "ab", "uo"], [[0, 3], [1, 2], [0, 1]], [3, 1, 2]),
            (["apple", "oreo", "untie", "straw"], [[0, 3], [0, 1]], [3, 2]),
            (
                ["elephant", "ice", "owl", "umbrella", "egg"],
                [[0, 1], [1, 3], [2, 4], [0, 4]],
                [1, 2, 1, 2],
            ),
            (["ai", "bq", "ea"], [[0, 0], [0, 0], [2, 2], [2, 2], [1, 1]], [1, 1, 1, 1, 0]),
            (["cat", "ape", "dog", "emu"], [[0, 3], [1, 2]], [2, 1]),
            (["mfac", "gs", "udq", "r", "ira"], [[4, 4]], [1]),
            (["znb", "q"], [[1, 1], [0, 0], [1, 1], [1, 1]], [0, 0, 0, 0]),
            (
                ["egv", "qqg", "y", "xf", "lixu", "qmr", "lqw", "uo"],
                [[2, 4], [1, 6], [7, 7]],
                [0, 0, 1],
            ),
            (["uhc", "chc"], [[0, 0], [0, 1], [1, 1]], [0, 0, 0]),
            (
                ["ormp", "r", "fsj", "zk", "emkl"],
                [[1, 3], [4, 4], [4, 4], [1, 1], [4, 4]],
                [0, 0, 0, 0, 0],
            ),
            (["vg", "ypww", "mwf"], [[1, 2], [2, 2], [1, 1]], [0, 0, 0]),
            (["bag", "t", "tkrf", "ew"], [[0, 3]], [0]),
            (["g", "b"], [[0, 1], [1, 1]], [0, 0]),
        ],
    )
    def test_vowel_strings(self, words: list[str], queries: list[list[int]], expected: list[int]):
        result = run_vowel_strings(Solution, words, queries)
        assert_vowel_strings(result, expected)
