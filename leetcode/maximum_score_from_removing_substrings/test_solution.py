import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_gain, run_maximum_gain
from .solution import Solution


class TestMaximumScoreFromRemovingSubstrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, x, y, expected",
        [
            ("cdbcbbaaabab", 4, 5, 19),
            ("aabbaaxybbaabb", 5, 4, 20),
            ("ab", 1, 1, 1),
            ("ba", 3, 4, 4),
            ("abab", 2, 1, 4),
            ("aabb", 3, 2, 6),
            ("bbaa", 3, 2, 4),
            ("abc", 5, 4, 5),
            ("a", 5, 4, 0),
            ("bbbaaa", 4, 5, 15),
            ("aaaabbbb", 5, 4, 20),
            ("ababab", 1, 10, 21),
            ("bababa", 10, 1, 21),
            ("aaocnbbaabaaadbabpaabbbgwlansaabbuaaaara", 10000, 1, 60002),
            ("adababbaoybanbdaaaaqaaaabbbbbaaababaaaabaabbbgbbfgaubba", 1, 10000, 120004),
            ("aalbaaaaaaaaabaabdcblhbebybfrbbababbbaaaaombwabbaaaabbb", 10000, 1, 80006),
        ],
    )
    def test_maximum_gain(self, s: str, x: int, y: int, expected: int):
        result = run_maximum_gain(Solution, s, x, y)
        assert_maximum_gain(result, expected)
