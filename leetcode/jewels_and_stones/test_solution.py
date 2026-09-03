import pytest

from leetcode_py import logged_test

from .helpers import assert_num_jewels_in_stones, run_num_jewels_in_stones
from .solution import Solution


class TestJewelsAndStones:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "jewels, stones, expected",
        [
            ("aA", "aAAbbbb", 3),
            ("z", "ZZ", 0),
            ("a", "a", 1),
            ("a", "A", 0),
            ("a", "b", 0),
            ("abc", "abcabc", 6),
            ("ABC", "abcABC", 3),
            ("aA", "aAaAaA", 6),
            ("z", "z", 1),
            ("xy", "xyxyx", 5),
            ("Ab", "aAbBbA", 4),
            ("q", "QqQq", 2),
            ("mno", "mnopqrstuvwxyz", 3),
            ("bc", "cbcb", 4),
            ("Jj", "jJjJjJ", 6),
            ("fG", "fGfGfGfG", 8),
            ("t", "abcdefghij", 0),
            ("aeiou", "bcdfghjklmnp", 0),
            ("w", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww", 50),
            ("abcdefghij", "jihgfedcba", 10),
        ],
    )
    def test_num_jewels_in_stones(self, jewels: str, stones: str, expected: int):
        result = run_num_jewels_in_stones(Solution, jewels, stones)
        assert_num_jewels_in_stones(result, expected)
