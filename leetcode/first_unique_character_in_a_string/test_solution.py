import pytest

from leetcode_py import logged_test

from .helpers import assert_first_uniq_char, run_first_uniq_char
from .solution import Solution


class TestFirstUniqueCharacterInAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("leetcode", 0),
            ("loveleetcode", 2),
            ("aabb", -1),
            ("a", 0),
            ("aa", -1),
            ("abcabc", -1),
            ("abc", 0),
            ("aadadaad", -1),
            ("z", 0),
            ("zz", -1),
            ("xyyx", -1),
            ("xyx", 1),
            ("aab", 2),
            ("aba", 1),
            ("aaabbb", -1),
            ("aaab", 3),
            ("abcab", 2),
            ("aabbc", 4),
            ("aabcc", 2),
            ("aabbb", -1),
        ],
    )
    def test_first_uniq_char(self, s: str, expected: int):
        result = run_first_uniq_char(Solution, s)
        assert_first_uniq_char(result, expected)
