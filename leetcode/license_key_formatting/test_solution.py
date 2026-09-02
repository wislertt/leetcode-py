import pytest

from leetcode_py import logged_test

from .helpers import assert_license_key_formatting, run_license_key_formatting
from .solution import Solution


class TestLicenseKeyFormatting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("5F3Z-2e-9-w", 4, "5F3Z-2E9W"),
            ("2-5g-3-J", 2, "2-5G-3J"),
            ("2-4A0r7-4k", 4, "24A0-R74K"),
            ("2-4A0r7-4k", 3, "24-A0R-74K"),
            ("a-a-a-a-", 1, "A-A-A-A"),
            ("a", 1, "A"),
            ("AB", 2, "AB"),
            ("AB", 1, "A-B"),
            ("abc", 5, "ABC"),
            ("5F3Z-2e-9-w", 3, "5F-3Z2-E9W"),
            ("2-5g-3-J", 3, "25-G3J"),
            ("0-0", 1, "0-0"),
            ("---A---B", 2, "AB"),
            ("---A---B", 1, "A-B"),
            ("AbCdEfGh", 2, "AB-CD-EF-GH"),
            ("J-5k-3z-Q-9", 4, "J5K-3ZQ9"),
            ("8-5g-3-J-1", 2, "85-G3-J1"),
            ("ZZ-YY-XX", 3, "ZZY-YXX"),
        ],
    )
    def test_license_key_formatting(self, s: str, k: int, expected: str):
        result = run_license_key_formatting(Solution, s, k)
        assert_license_key_formatting(result, expected)
