import pytest

from leetcode_py import logged_test

from .helpers import assert_regions_by_slashes, run_regions_by_slashes
from .solution import Solution


class TestRegionsCutBySlashes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([" /", "/ "], 2),
            ([" /", "  "], 1),
            (["/\\", "\\/"], 5),
            (["  ", "  "], 1),
            (["/"], 2),
            (["\\"], 2),
            ([" "], 1),
            (["//", "/ "], 3),
            (["\\/", "/\\"], 4),
            ([" / ", "/  ", "  /"], 3),
            (["/\\/", " \\/", "/  "], 3),
            (["\\\\", "  "], 2),
            (["\\\\", "\\\\"], 4),
            ([" /\\ ", "\\ / ", "/  \\", " \\/ "], 2),
            (["/\\/\\", "\\ / ", " \\\\ ", "\\\\  "], 5),
            (["/\\/", " \\/", "/  "], 3),
        ],
    )
    def test_regions_by_slashes(self, grid: list[str], expected: int):
        result = run_regions_by_slashes(Solution, grid)
        assert_regions_by_slashes(result, expected)
