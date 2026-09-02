import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_path_value, run_largest_path_value
from .solution import Solution


class TestLargestColorValueInADirectedGraph:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "colors, edges, expected",
        [
            ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3),
            ("a", [[0, 0]], -1),
            ("a", [], 1),
            ("ab", [[0, 1], [1, 0]], -1),
            ("abc", [[0, 1], [1, 2], [2, 0]], -1),
            ("aa", [[0, 1]], 2),
            ("abca", [[0, 1], [1, 2], [2, 3]], 2),
            ("aab", [[0, 1], [0, 2], [1, 2]], 2),
            ("zzzzz", [[0, 1], [1, 2], [2, 3], [3, 4]], 5),
            ("abcabc", [[0, 3], [1, 4], [2, 5]], 2),
            ("ab", [[0, 1], [0, 1]], 1),
            ("abcd", [[0, 1], [2, 3], [1, 1]], -1),
            ("aabbb", [[0, 1], [1, 2], [2, 3], [3, 4]], 3),
            ("xyzxyz", [[0, 1], [1, 2], [3, 4], [4, 5], [2, 3]], 2),
            ("hgfn", [[0, 1], [1, 2], [2, 3], [3, 0]], -1),
            ("cbbb", [[0, 3]], 1),
            ("cbzac", [[0, 2], [1, 3]], 1),
            ("zabzz", [[1, 4]], 1),
            ("bzzac", [[1, 2], [1, 4], [2, 3], [3, 4]], 2),
            ("zazz", [[0, 2], [0, 3], [1, 2]], 2),
            ("zaa", [[1, 2]], 2),
            ("zazzza", [[0, 4], [0, 5], [3, 5]], 2),
            ("acz", [[0, 1]], 1),
            ("caa", [[0, 2]], 1),
            ("cbzzc", [[0, 2], [1, 4], [2, 4]], 2),
            ("zbac", [[0, 1]], 1),
            ("czabc", [[0, 1], [0, 2], [1, 2], [1, 4], [2, 4], [3, 4]], 2),
        ],
    )
    def test_largest_path_value(self, colors: str, edges: list[list[int]], expected: int):
        result = run_largest_path_value(Solution, colors, edges)
        assert_largest_path_value(result, expected)
