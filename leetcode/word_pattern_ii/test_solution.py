import pytest

from leetcode_py import logged_test

from .helpers import assert_word_pattern_match, run_word_pattern_match
from .solution import Solution


class TestWordPatternII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pattern, s, expected",
        [
            ("abab", "redblueredblue", True),
            ("aaaa", "asdasdasdasd", True),
            ("aabb", "xyzabcxzyabc", False),
            ("a", "a", True),
            ("a", "z", True),
            ("ab", "aa", False),
            ("ab", "ab", True),
            ("abba", "dogcatcatdog", True),
            ("abba", "dogdogdogdog", False),
            ("aaaa", "aaaaaaaa", True),
            ("abc", "ab", False),
            ("ab", "aaa", True),
            ("ab", "aabb", True),
            ("abab", "xyxy", True),
            ("a", "ab", True),
            ("abba", "dogcatcatfish", False),
            ("aa", "aa", True),
            ("ab", "aab", True),
        ],
    )
    def test_word_pattern_match(self, pattern: str, s: str, expected: bool):
        result = run_word_pattern_match(Solution, pattern, s)
        assert_word_pattern_match(result, expected)
