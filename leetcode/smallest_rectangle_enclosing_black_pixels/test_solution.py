import pytest

from leetcode_py import logged_test

from .helpers import assert_min_area, run_min_area
from .solution import Solution


class TestSmallestRectangleEnclosingBlackPixels:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "image, x, y, expected",
        [
            ([["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2, 6),
            ([["1"]], 0, 0, 1),
            ([["1", "1", "1"]], 0, 1, 3),
            ([["1"], ["1"], ["1"]], 1, 0, 3),
            ([["1", "1"], ["1", "1"]], 0, 0, 4),
            ([["0", "0"], ["1", "0"]], 1, 0, 1),
            ([["0", "0", "0"], ["0", "1", "0"]], 1, 1, 1),
            ([["1", "0", "0"], ["1", "1", "0"], ["1", "1", "1"]], 2, 2, 9),
            ([["0", "1", "0"], ["0", "1", "0"]], 0, 1, 2),
            (
                [
                    ["0", "0", "0", "0"],
                    ["0", "1", "1", "0"],
                    ["0", "1", "1", "0"],
                    ["0", "0", "0", "0"],
                ],
                1,
                1,
                4,
            ),
            ([["1", "1", "1", "1", "1"]], 0, 3, 5),
            ([["0", "1"], ["0", "1"], ["0", "1"], ["0", "1"]], 3, 1, 4),
            ([["0", "0"], ["0", "1"]], 1, 1, 1),
            (
                [
                    ["1", "1", "0", "0"],
                    ["1", "1", "0", "0"],
                    ["0", "0", "0", "0"],
                    ["0", "0", "0", "0"],
                ],
                0,
                0,
                4,
            ),
            ([["0", "0", "1"], ["0", "1", "1"]], 0, 2, 4),
        ],
    )
    def test_min_area(self, image: list[list[str]], x: int, y: int, expected: int):
        result = run_min_area(Solution, image, x, y)
        assert_min_area(result, expected)
