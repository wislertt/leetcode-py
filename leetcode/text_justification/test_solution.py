import pytest

from leetcode_py import logged_test

from .helpers import assert_full_justify, run_full_justify
from .solution import Solution


class TestTextJustification:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, max_width, expected",
        [
            (
                ["This", "is", "an", "example", "of", "text", "justification."],
                16,
                ["This    is    an", "example  of text", "justification.  "],
            ),
            (
                ["What", "must", "be", "acknowledgment", "shall", "be"],
                16,
                ["What   must   be", "acknowledgment  ", "shall be        "],
            ),
            (
                [
                    "Science",
                    "is",
                    "what",
                    "we",
                    "understand",
                    "well",
                    "enough",
                    "to",
                    "explain",
                    "to",
                    "a",
                    "computer.",
                    "Art",
                    "is",
                    "everything",
                    "else",
                    "we",
                    "do",
                ],
                20,
                [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  ",
                ],
            ),
            (["hello"], 10, ["hello     "]),
            (["a"], 1, ["a"]),
            (["a", "b", "c", "d"], 3, ["a b", "c d"]),
            (["a", "b", "c"], 5, ["a b c"]),
            (["a", "b", "c"], 4, ["a  b", "c   "]),
            (["listen", "to", "the", "rain"], 6, ["listen", "to the", "rain  "]),
            (["a", "b", "c", "d"], 7, ["a b c d"]),
            (["aa", "bb", "cc", "dd"], 8, ["aa bb cc", "dd      "]),
            (["a", "b", "c", "xxx"], 7, ["a  b  c", "xxx    "]),
            (["a", "b", "c", "d", "e"], 8, ["a  b c d", "e       "]),
            (["abcde"], 5, ["abcde"]),
            (["a", "b"], 1, ["a", "b"]),
            (["aaa", "bbb"], 3, ["aaa", "bbb"]),
            (["to", "be", "or", "not", "to", "be"], 6, ["to  be", "or not", "to be "]),
            (["x", "yy", "zzz", "wwww"], 7, ["x    yy", "zzz    ", "wwww   "]),
        ],
    )
    def test_full_justify(self, words: list[str], max_width: int, expected: list[str]):
        result = run_full_justify(Solution, words, max_width)
        assert_full_justify(result, expected)
