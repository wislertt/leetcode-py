import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_way, run_shortest_way
from .solution import Solution


class TestShortestWayToFormString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "source, target, expected",
        [
            ("abc", "abcbc", 2),
            ("abc", "acdbc", -1),
            ("xyz", "xzyxz", 3),
            ("abc", "abc", 1),
            ("a", "aaaa", 4),
            ("abc", "d", -1),
            ("abc", "cba", 3),
            ("ab", "ba", 2),
            ("xyzx", "xzxyxzxz", 4),
            ("bbbb", "b", 1),
            ("meat", "meteoretemtt", -1),
            ("kok", "kokokok", 3),
            ("abcabc", "abcabcabcabc", 2),
            ("aaaa", "aa", 1),
        ],
    )
    def test_shortest_way(self, source: str, target: str, expected: int):
        result = run_shortest_way(Solution, source, target)
        assert_shortest_way(result, expected)
