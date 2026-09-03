import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_to_char, run_shortest_to_char
from .solution import Solution


class TestShortestDistanceToACharacter:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, c, expected",
        [
            ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
            ("aaab", "b", [3, 2, 1, 0]),
            ("a", "a", [0]),
            ("ab", "a", [0, 1]),
            ("ab", "b", [1, 0]),
            ("aaabaaa", "b", [3, 2, 1, 0, 1, 2, 3]),
            ("bbbbb", "b", [0, 0, 0, 0, 0]),
            ("abcabc", "a", [0, 1, 1, 0, 1, 2]),
            ("cbacba", "a", [2, 1, 0, 1, 1, 0]),
            ("aabaa", "b", [2, 1, 0, 1, 2]),
            ("baaab", "a", [1, 0, 0, 0, 1]),
            ("jylhdzdmuwvriizwl", "z", [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 1, 2]),
            ("xjgkwixdamzn", "z", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]),
            ("zq", "z", [0, 1]),
            ("qmpza", "z", [3, 2, 1, 0, 1]),
            ("fvpjsorzswpcculmvf", "z", [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ("zstjfivf", "z", [0, 1, 2, 3, 4, 5, 6, 7]),
            ("egftlxyidzza", "z", [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1]),
            ("juzirkbjxoh", "z", [2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
            ("pbktizonjiog", "z", [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]),
        ],
    )
    def test_shortest_to_char(self, s: str, c: str, expected: list[int]):
        result = run_shortest_to_char(Solution, s, c)
        assert_shortest_to_char(result, expected)
