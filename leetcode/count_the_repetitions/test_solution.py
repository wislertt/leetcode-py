import pytest

from leetcode_py import logged_test

from .helpers import assert_get_max_repetitions, run_get_max_repetitions
from .solution import Solution


class TestCountTheRepetitions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, n1, s2, n2, expected",
        [
            ("acb", 4, "ab", 2, 2),
            ("acb", 1, "acb", 1, 1),
            ("aaa", 3, "aaa", 1, 3),
            ("abc", 1, "bca", 1, 0),
            ("ab", 5, "ba", 2, 2),
            ("abab", 3, "ab", 2, 3),
            ("aaa", 20, "aa", 1, 30),
            ("aaa", 5, "aaaaa", 1, 3),
            ("abcabc", 3, "cba", 2, 1),
            ("abc", 4, "d", 1, 0),
            ("a", 1000000, "a", 1, 1000000),
            ("abc", 1000000, "abc", 1000000, 1),
            ("abcd", 100, "dcba", 1000000, 0),
            ("aa", 1, "aaaa", 1, 0),
            ("abc", 100, "cab", 1000000, 0),
            ("ba", 1000, "ab", 1000, 0),
            ("abcde", 40, "ace", 10, 4),
            ("xyz", 7, "xyxyx", 1, 2),
            ("aaa", 999983, "aaaa", 1000000, 0),
            ("ab", 1000000, "ab", 3, 333333),
        ],
    )
    def test_get_max_repetitions(self, s1: str, n1: int, s2: str, n2: int, expected: int):
        result = run_get_max_repetitions(Solution, s1, n1, s2, n2)
        assert_get_max_repetitions(result, expected)
