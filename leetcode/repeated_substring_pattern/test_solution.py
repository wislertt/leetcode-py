import pytest

from leetcode_py import logged_test

from .helpers import assert_repeated_substring_pattern, run_repeated_substring_pattern
from .solution import Solution


class TestRepeatedSubstringPattern:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abab", True),
            ("aba", False),
            ("abcabcabcabc", True),
            ("a", False),
            ("aa", True),
            ("ab", False),
            ("aaa", True),
            ("abcabc", True),
            ("abac", False),
            ("aabaab", True),
            ("abcabcabc", True),
            ("xyxyxyxy", True),
            ("abcabdabcabd", True),
            ("abababababababababababababababababababababababababababababab", True),
            ("aabaabaab", True),
            ("abcabd", False),
            ("ababababab", True),
            ("zzzzz", True),
            ("ababab", True),
            ("aabaabaa", False),
            ("babbbdaaaab", False),
            ("bcabaacaaa", False),
            ("abaaaabbbab", False),
            ("bbaaabacbadc", False),
            ("c", False),
            ("d", False),
            ("ba", False),
            ("abadbaacabab", False),
        ],
    )
    def test_repeated_substring_pattern(self, s: str, expected: bool):
        result = run_repeated_substring_pattern(Solution, s)
        assert_repeated_substring_pattern(result, expected)
