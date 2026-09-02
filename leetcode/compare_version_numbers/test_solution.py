import pytest

from leetcode_py import logged_test

from .helpers import assert_compare_version, run_compare_version
from .solution import Solution


class TestCompareVersionNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "version1, version2, expected",
        [
            ("1.2", "1.10", -1),
            ("1.01", "1.001", 0),
            ("1.0", "1.0.0.0", 0),
            ("0.1", "1.1", -1),
            ("7.5.2.4", "7.5.3", -1),
            ("2.0", "1.0", 1),
            ("1", "1.0.0", 0),
            ("1.0.0", "1", 0),
            ("0.0.1", "0.0.1", 0),
            ("10.4.4", "10.4.4.0", 0),
            ("1.2.3.4.5", "1.2.3.4", 1),
            ("001.000.1", "1.0.1", 0),
            ("2.0.1", "1.9.9", 1),
            ("1.00000000001", "1.0", 1),
            ("0.0.0", "0", 0),
            ("3.4.5.6.7.8", "3.4.5.6.7.9", -1),
            ("3", "4.11.20.003", -1),
            ("38.026", "24.6.31.16.33", 1),
            ("19.38", "024", -1),
            ("7.21.19", "29.11.40", -1),
        ],
    )
    def test_compare_version(self, version1: str, version2: str, expected: int):
        result = run_compare_version(Solution, version1, version2)
        assert_compare_version(result, expected)
