import pytest

from leetcode_py import logged_test

from .helpers import assert_unique_morse_representations, run_unique_morse_representations
from .solution import Solution


class TestUniqueMorseCodeWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["gin", "zen", "gig", "msg"], 2),
            (["a"], 1),
            (["zocd", "gqkl"], 2),
            (["ab", "ba", "ab"], 2),
            (["abc", "bca", "cab"], 3),
            (["a", "b", "c", "d"], 4),
            (["aaaaaaaaaaaa"], 1),
            (["abcdefghijkl"], 1),
            (["aaa", "bbb", "ccc"], 3),
            (["cab", "abc", "bca"], 3),
            (["xyz"], 1),
            (["q", "z", "q"], 2),
            (["hello", "world"], 2),
            (["leetcode", "code", "leet"], 3),
            (["ab", "cd", "ef", "gh", "ij"], 5),
            (["aa", "bb", "cc", "aa"], 3),
            (["a", "a", "a", "a", "a"], 1),
            (["morse", "code", "words"], 3),
            (["zzzz", "yyyy"], 2),
            (["abcdefghijkl", "a", "zzzzzzzzzzzz"], 3),
            (["aa", "a", "aaa"], 3),
            (["xy", "yx"], 2),
            (["pqr", "qrp", "rpq"], 3),
            (["abcd", "dcba"], 2),
        ],
    )
    def test_unique_morse_representations(self, words: list[str], expected: int):
        result = run_unique_morse_representations(Solution, words)
        assert_unique_morse_representations(result, expected)
