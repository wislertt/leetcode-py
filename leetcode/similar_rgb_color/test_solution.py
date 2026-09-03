import pytest

from leetcode_py import logged_test

from .helpers import assert_similar_rgb, run_similar_rgb
from .solution import Solution


class TestSimilarRgbColor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "color, expected",
        [
            ("#09f166", "#11ee66"),
            ("#4e3fe1", "#5544dd"),
            ("#000000", "#000000"),
            ("#ffffff", "#ffffff"),
            ("#010101", "#000000"),
            ("#1a2b3c", "#223344"),
            ("#fefefe", "#ffffff"),
            ("#8899aa", "#8899aa"),
            ("#abcdef", "#aaccee"),
            ("#000001", "#000000"),
            ("#7f7f7f", "#777777"),
            ("#080808", "#000000"),
            ("#f0f0f0", "#eeeeee"),
            ("#123456", "#113355"),
            ("#deadbf", "#ddaabb"),
            ("#5c5c5c", "#555555"),
        ],
    )
    def test_similar_rgb(self, color: str, expected: str):
        result = run_similar_rgb(Solution, color)
        assert_similar_rgb(result, expected)
