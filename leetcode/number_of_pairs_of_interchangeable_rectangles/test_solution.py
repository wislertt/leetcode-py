import pytest

from leetcode_py import logged_test

from .helpers import assert_interchangeable_rectangles, run_interchangeable_rectangles
from .solution import Solution


class TestNumberOfPairsOfInterchangeableRectangles:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rectangles, expected",
        [
            ([[4, 8], [3, 6], [10, 20], [15, 30]], 6),
            ([[4, 5], [7, 8]], 0),
            ([[1, 1]], 0),
            ([[1, 1], [1, 1]], 1),
            ([[2, 4], [1, 2], [3, 6]], 3),
            ([[5, 5], [5, 5], [5, 5]], 3),
            ([[1, 2], [2, 1]], 0),
            ([[100000, 100000], [100000, 100000], [99999, 99998]], 1),
            ([[1, 100000], [1, 100000]], 1),
            ([[3, 4], [6, 8], [9, 12], [4, 3]], 3),
            ([[7, 13], [14, 26], [21, 39]], 3),
            ([[2, 3], [4, 6], [6, 9], [3, 5]], 3),
            ([[1, 1], [2, 2], [1, 1], [2, 2], [3, 3]], 10),
            ([[12, 18], [2, 3], [4, 6], [5, 7]], 3),
            ([[100000, 1], [100000, 1], [100000, 2]], 1),
            ([[1, 3], [2, 6], [3, 9], [4, 12], [5, 15], [6, 18]], 15),
            ([[15, 15]], 0),
            ([[2, 6], [8, 6], [4, 6], [6, 6], [8, 6]], 1),
            ([[2, 2]], 0),
            ([[21, 21], [21, 21], [21, 21], [14, 21]], 3),
        ],
    )
    def test_interchangeable_rectangles(self, rectangles: list[list[int]], expected: int):
        result = run_interchangeable_rectangles(Solution, rectangles)
        assert_interchangeable_rectangles(result, expected)
