import pytest

from leetcode_py import logged_test

from .helpers import assert_min_height_shelves, run_min_height_shelves
from .solution import Solution


class TestFillingBookcaseShelves:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "books, shelf_width, expected",
        [
            ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4, 6),
            ([[1, 3], [2, 4], [3, 2]], 6, 4),
            ([[1, 1]], 1, 1),
            ([[1, 1]], 5, 1),
            ([[1, 1], [1, 1], [1, 1]], 1, 3),
            ([[2, 5], [2, 5]], 4, 5),
            ([[2, 5], [2, 5]], 2, 10),
            ([[1, 2], [2, 3], [1, 1], [3, 4], [1, 1]], 3, 9),
            ([[7, 3], [8, 7], [2, 7], [2, 5]], 10, 15),
            ([[1, 1], [2, 2], [3, 3], [4, 4]], 10, 4),
            ([[5, 5], [5, 5], [5, 5]], 5, 15),
            ([[3, 2], [3, 20], [1, 1], [4, 4], [2, 10]], 7, 30),
        ],
    )
    def test_min_height_shelves(self, books: list[list[int]], shelf_width: int, expected: int):
        result = run_min_height_shelves(Solution, books, shelf_width)
        assert_min_height_shelves(result, expected)
