import pytest

from leetcode_py import logged_test

from .helpers import assert_word_pattern, run_word_pattern
from .solution import Solution


class TestWordPattern:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pattern, s, expected",
        [
            ("abba", "dog cat cat dog", True),
            ("abba", "dog cat cat fish", False),
            ("aaaa", "dog cat cat dog", False),
            ("abba", "dog dog dog dog", False),
            ("a", "a", True),
            ("a", "b", True),
            ("ab", "dog cat", True),
            ("ab", "cat dog", True),
            ("aa", "dog dog", True),
            ("aa", "dog cat", False),
            ("abc", "dog cat dog", False),
            ("abc", "dog cat fish", True),
            ("abba", "dog cat cat", False),
            ("abba", "dog cat cat dog extra", False),
            ("aaaa", "dog dog dog dog", True),
            ("abcabc", "dog cat fish dog cat fish", True),
            ("abcabc", "dog cat fish cat fish dog", False),
            ("ab", "dog dog", False),
            ("aabb", "dog dog cat cat", True),
            ("abba", "dog cat fish dog", False),
        ],
    )
    def test_word_pattern(self, pattern: str, s: str, expected: bool):
        result = run_word_pattern(Solution, pattern, s)
        assert_word_pattern(result, expected)
