import pytest

from leetcode_py import logged_test

from .helpers import assert_large_group_positions, run_large_group_positions
from .solution import Solution


class TestPositionsOfLargeGroups:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abbxxxxzzy", [[3, 6]]),
            ("abc", []),
            ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
            ("aaa", [[0, 2]]),
            ("a", []),
            ("aa", []),
            ("ab", []),
            ("aaabbb", [[0, 2], [3, 5]]),
            ("aaaabbbb", [[0, 3], [4, 7]]),
            ("abccc", [[2, 4]]),
            ("cccab", [[0, 2]]),
            ("aaabbbaaa", [[0, 2], [3, 5], [6, 8]]),
            ("aabbccdd", []),
            ("abbbbc", [[1, 4]]),
            ("aaaaa", [[0, 4]]),
            ("aabaaabbb", [[3, 5], [6, 8]]),
            ("bccd", []),
            ("b", []),
            ("aecdcadcccdecd", [[7, 9]]),
            ("edeeaab", []),
        ],
    )
    def test_large_group_positions(self, s: str, expected: list[list[int]]):
        result = run_large_group_positions(Solution, s)
        assert_large_group_positions(result, expected)
