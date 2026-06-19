import pytest

from leetcode_py import logged_test

from .helpers import assert_min_distance, run_min_distance
from .solution import Solution


class TestEditDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            ("horse", "ros", 3),
            ("intention", "execution", 5),
            ("", "", 0),
            ("", "a", 1),
            ("a", "", 1),
            ("a", "a", 0),
            ("ab", "a", 1),
            ("a", "ab", 1),
            ("ab", "ba", 2),
            ("abc", "abc", 0),
            ("abc", "abd", 1),
            ("kitten", "sitting", 3),
            ("saturday", "sunday", 3),
            ("", "abc", 3),
        ],
    )
    def test_min_distance(self, word1: str, word2: str, expected: int):
        result = run_min_distance(Solution, word1, word2)
        assert_min_distance(result, expected)
