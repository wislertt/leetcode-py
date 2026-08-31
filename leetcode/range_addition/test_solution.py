import pytest

from leetcode_py import logged_test

from .helpers import assert_get_modified_array, run_get_modified_array
from .solution import Solution


class TestRangeAddition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "length, updates, expected",
        [
            (5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]], [-2, 0, 3, 5, 3]),
            (10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]], [0, -4, 2, 2, 2, 4, 4, -4, -4, -4]),
            (1, [], [0]),
            (1, [[0, 0, 5]], [5]),
            (3, [[0, 2, 1], [0, 2, 1], [0, 2, 1]], [3, 3, 3]),
            (4, [[0, 0, -3], [3, 3, 7]], [-3, 0, 0, 7]),
            (5, [[4, 4, 1000]], [0, 0, 0, 0, 1000]),
            (5, [[0, 4, -1000]], [-1000, -1000, -1000, -1000, -1000]),
            (6, [[0, 5, 1], [1, 4, 2], [2, 3, 3], [3, 3, -6]], [1, 3, 6, 0, 3, 1]),
            (2, [[0, 1, 1], [1, 1, 2], [0, 0, -4]], [-3, 3]),
            (7, [[3, 5, 2]], [0, 0, 0, 2, 2, 2, 0]),
            (8, [], [0, 0, 0, 0, 0, 0, 0, 0]),
            (5, [[0, 4, 1000], [0, 4, -1000]], [0, 0, 0, 0, 0]),
            (6, [[2, 2, 9]], [0, 0, 9, 0, 0, 0]),
            (4, [[0, 3, 1], [1, 2, -2]], [1, -1, -1, 1]),
            (9, [[0, 8, 3], [4, 8, -1], [2, 6, 7]], [3, 3, 10, 10, 9, 9, 9, 2, 2]),
        ],
    )
    def test_get_modified_array(self, length: int, updates: list[list[int]], expected: list[int]):
        result = run_get_modified_array(Solution, length, updates)
        assert_get_modified_array(result, expected)
