import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_max_length_between_equal_characters,
    run_max_length_between_equal_characters,
)
from .solution import Solution


class TestLargestSubstringBetweenTwoEqualCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aa", 0),
            ("abca", 2),
            ("cbzxy", -1),
            ("a", -1),
            ("abcba", 3),
            ("aaaa", 2),
            ("ab", -1),
            ("abcdefga", 6),
            ("zz", 0),
            ("xyzy", 1),
            ("leetcode", 5),
            ("bba", 0),
            ("ahed", -1),
            ("ffdecbebb", 2),
            ("edehahfd", 5),
            ("hec", -1),
            ("bddggac", 0),
            ("bebggga", 1),
        ],
    )
    def test_max_length_between_equal_characters(self, s: str, expected: int):
        result = run_max_length_between_equal_characters(Solution, s)
        assert_max_length_between_equal_characters(result, expected)
