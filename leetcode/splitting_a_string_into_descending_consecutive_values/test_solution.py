import pytest

from leetcode_py import logged_test

from .helpers import assert_split_string, run_split_string
from .solution import Solution


class TestSplittingAStringIntoDescendingConsecutiveValues:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1234", False),
            ("050043", True),
            ("9080701", False),
            ("0090089", True),
            ("001", False),
            ("10", True),
            ("21", True),
            ("32", True),
            ("00", False),
            ("5", False),
            ("0", False),
            ("9876543210", True),
            ("321", True),
            ("534", False),
            ("0435", False),
            ("1009998", True),
            ("12345", False),
            ("4321098", False),
            ("99897", False),
            ("0000", False),
            ("20201", False),
            ("1099897", False),
        ],
    )
    def test_split_string(self, s: str, expected: bool):
        result = run_split_string(Solution, s)
        assert_split_string(result, expected)
