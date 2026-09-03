import pytest

from leetcode_py import logged_test

from .helpers import assert_expressive_words, run_expressive_words
from .solution import Solution


class TestExpressiveWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, words, expected",
        [
            ("heeellooo", ["hello", "hi", "helo"], 1),
            ("zzzzzyyyyy", ["zzyy", "zy", "zyy"], 3),
            ("helllllooo", ["hello"], 1),
            ("helloo", ["hello"], 0),
            ("aaa", ["aa"], 1),
            ("aaa", ["a"], 1),
            ("aaa", ["aaaaa"], 0),
            ("aaaaa", ["aa"], 1),
            ("a", ["aa"], 0),
            ("a", ["a"], 1),
            ("abc", ["abc"], 1),
            ("abc", ["ab"], 0),
            ("aaab", ["ab"], 1),
            ("aaa", ["bbb"], 0),
            ("aaa", ["a", "b"], 1),
            ("aaa", ["ab"], 0),
            ("aaa", ["aa", "aaa", "aaaa", "a"], 3),
            ("aaaaaaaaaaaaaaaaaaaa", ["a", "aaaaaaaaaaaaaaaaaa"], 2),
            ("heeellooo", ["hello", "heeello", "hell", "heello", "heeellooo"], 4),
            ("dddiiiinnsssssyyyy", ["dinnssoyy", "diinnsstyyyy"], 0),
        ],
    )
    def test_expressive_words(self, s: str, words: list[str], expected: int):
        result = run_expressive_words(Solution, s, words)
        assert_expressive_words(result, expected)
