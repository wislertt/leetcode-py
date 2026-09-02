import pytest

from leetcode_py import logged_test

from .helpers import assert_is_path_crossing, run_is_path_crossing
from .solution import Solution


class TestPathCrossing:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "path, expected",
        [
            ("NES", False),
            ("NESWW", True),
            ("N", False),
            ("S", False),
            ("E", False),
            ("W", False),
            ("NS", True),
            ("SN", True),
            ("EW", True),
            ("WE", True),
            ("NESW", True),
            ("NNEESS", False),
            ("SSSS", False),
            ("NNNN", False),
            ("EN", False),
            ("NWSE", True),
            ("NWSSEE", False),
            ("EESWWN", True),
        ],
    )
    def test_is_path_crossing(self, path: str, expected: bool):
        result = run_is_path_crossing(Solution, path)
        assert_is_path_crossing(result, expected)
