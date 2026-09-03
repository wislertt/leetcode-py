import pytest

from leetcode_py import logged_test

from .helpers import assert_find_black_pixel, run_find_black_pixel
from .solution import Solution


class TestLonelyPixelII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "picture, target, expected",
        [
            ([["W", "W", "B"], ["W", "W", "B"], ["W", "W", "B"]], 1, 0),
            ([["W", "B", "W"], ["W", "B", "W"], ["W", "B", "W"]], 1, 0),
            ([["W", "B", "W"], ["W", "B", "W"], ["W", "B", "W"]], 2, 0),
            ([["W", "B", "W"], ["W", "B", "W"], ["W", "B", "W"]], 3, 0),
            ([["B", "W"], ["B", "W"]], 1, 0),
            ([["B", "W"], ["B", "W"]], 2, 0),
            ([["B", "W", "B"], ["B", "W", "B"]], 1, 0),
            ([["B", "W", "B"], ["B", "W", "B"]], 2, 4),
            ([["B"]], 1, 1),
            ([["W"]], 1, 0),
            ([["B", "B"], ["B", "B"]], 2, 4),
            ([["B", "B", "W"], ["B", "W", "B"]], 1, 0),
            ([["B", "W", "B"], ["B", "W", "B"], ["W", "B", "W"]], 2, 4),
            ([["B", "W"], ["W", "B"]], 1, 2),
            ([["B", "W", "B"], ["B", "B", "W"]], 2, 0),
            ([["W", "B", "B"], ["B", "B", "W"]], 2, 0),
            ([["W", "W", "B", "B"], ["W", "W", "B", "B"]], 2, 4),
            ([["B", "W", "B"], ["W", "B", "B"], ["B", "W", "B"]], 1, 0),
            ([["B", "W"], ["W", "B"], ["B", "W"], ["W", "B"]], 1, 0),
            ([["W", "B"], ["W", "B"], ["W", "B"]], 1, 0),
            ([["W", "W"], ["B", "B"], ["B", "W"], ["B", "B"]], 1, 0),
            ([["B"], ["W"], ["B"]], 1, 0),
            ([["B", "W"]], 1, 1),
            ([["B", "W"], ["W", "W"], ["W", "B"]], 1, 2),
            ([["W", "B"], ["W", "B"], ["W", "B"], ["W", "W"]], 2, 0),
            (
                [
                    ["W", "W", "B", "W"],
                    ["W", "B", "B", "W"],
                    ["B", "B", "W", "W"],
                    ["B", "W", "W", "B"],
                ],
                2,
                0,
            ),
            ([["B", "W"], ["B", "B"], ["B", "B"]], 2, 2),
            ([["B"], ["B"], ["W"]], 1, 0),
            ([["B"], ["B"], ["W"], ["W"]], 1, 0),
            ([["W", "W"]], 1, 0),
            ([["W", "B", "W"]], 1, 1),
            (
                [
                    ["W", "B", "B", "B"],
                    ["W", "B", "W", "B"],
                    ["B", "W", "B", "B"],
                    ["W", "B", "B", "B"],
                ],
                1,
                0,
            ),
            ([["W"], ["W"], ["W"]], 1, 0),
            ([["B", "W", "B", "B"], ["W", "B", "B", "B"]], 1, 0),
            ([["B", "W", "W"]], 1, 1),
            ([["B", "B"], ["W", "W"]], 1, 0),
        ],
    )
    def test_find_black_pixel(self, picture: list[list[str]], target: int, expected: int):
        result = run_find_black_pixel(Solution, picture, target)
        assert_find_black_pixel(result, expected)
