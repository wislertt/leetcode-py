import pytest

from leetcode_py import logged_test

from .helpers import assert_min_flips_mono_increasing, run_min_flips_mono_increasing
from .solution import Solution


class TestFlipStringToMonotoneIncreasing:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("00110", 1),
            ("010110", 2),
            ("00011000", 2),
            ("0", 0),
            ("1", 0),
            ("10", 1),
            ("01", 0),
            ("11", 0),
            ("00", 0),
            ("110", 1),
            ("0101", 1),
            ("101010", 3),
            ("0000", 0),
            ("1111", 0),
            ("0100110", 2),
            ("10011111110010111011", 5),
        ],
    )
    def test_min_flips_mono_increasing(self, s: str, expected: int):
        result = run_min_flips_mono_increasing(Solution, s)
        assert_min_flips_mono_increasing(result, expected)
