import pytest

from leetcode_py import logged_test

from .helpers import assert_find_lonely_pixel, run_find_lonely_pixel
from .solution import Solution


class TestLonelyPixelI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "picture, expected",
        [
            ([["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]], 3),
            ([["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]], 0),
            ([["B"]], 1),
            ([["W"]], 0),
            ([["B", "W"], ["W", "B"]], 2),
            ([["B", "B"], ["W", "W"]], 0),
            ([["W", "W"], ["W", "B"]], 1),
            ([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]], 1),
            (
                [
                    ["W", "B", "W", "B"],
                    ["B", "W", "B", "W"],
                    ["W", "B", "W", "B"],
                    ["W", "W", "W", "W"],
                ],
                0,
            ),
            ([["B", "B", "W"], ["W", "W", "B"], ["B", "W", "W"]], 1),
            ([["W", "W", "W", "W"]], 0),
            ([["B", "B", "B", "B"]], 0),
        ],
    )
    def test_find_lonely_pixel(self, picture: list[list[str]], expected: int):
        result = run_find_lonely_pixel(Solution, picture)
        assert_find_lonely_pixel(result, expected)
