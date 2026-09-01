import pytest

from leetcode_py import logged_test

from .helpers import assert_can_construct, run_can_construct
from .solution import Solution


class TestConstructKPalindromeStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("annabelle", 2, True),
            ("leetcode", 3, False),
            ("true", 4, True),
            ("a", 1, True),
            ("ab", 1, False),
            ("ab", 2, True),
            ("aa", 1, True),
            ("aaa", 1, True),
            ("abc", 3, True),
            ("abc", 2, False),
            ("aabb", 1, True),
            ("aabbcc", 2, True),
            ("abcde", 5, True),
            ("abcde", 4, False),
            ("aaaa", 3, True),
            ("aaaa", 4, True),
            ("abcabc", 3, True),
            ("racecar", 1, True),
            ("ccb", 3, True),
            ("ddadbadcbaba", 8, True),
            ("bbaccac", 7, True),
            ("cddaaccd", 7, True),
        ],
    )
    def test_can_construct(self, s: str, k: int, expected: bool):
        result = run_can_construct(Solution, s, k)
        assert_can_construct(result, expected)
