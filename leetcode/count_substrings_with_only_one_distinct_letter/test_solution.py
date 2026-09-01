import pytest

from leetcode_py import logged_test

from .helpers import assert_count_letters, run_count_letters
from .solution import Solution


class TestCountSubstringsWithOnlyOneDistinctLetter:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aaaba", 8),
            ("aaaaaaaaaa", 55),
            ("a", 1),
            ("ab", 2),
            ("aa", 3),
            ("abc", 3),
            ("abab", 4),
            ("aabb", 6),
            ("abbbba", 12),
            ("aabaab", 8),
            ("zzzz", 10),
            ("abcabcabc", 9),
            ("mississippi", 14),
            ("xyxyx", 5),
            ("qqqww", 9),
            ("eeeeeeee", 36),
            ("bbaabba", 10),
            ("b", 1),
            ("aaab", 7),
            ("abaab", 6),
            ("aaababb", 11),
            ("aacabbbb", 15),
            ("aba", 3),
            ("bacba", 5),
        ],
    )
    def test_count_letters(self, s: str, expected: int):
        result = run_count_letters(Solution, s)
        assert_count_letters(result, expected)
