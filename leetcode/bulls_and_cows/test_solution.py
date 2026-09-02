import pytest

from leetcode_py import logged_test

from .helpers import assert_get_hint, run_get_hint
from .solution import Solution


class TestBullsAndCows:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "secret, guess, expected",
        [
            ("1807", "7810", "1A3B"),
            ("1123", "0111", "1A1B"),
            ("1", "1", "1A0B"),
            ("1", "0", "0A0B"),
            ("11", "10", "1A0B"),
            ("11", "11", "2A0B"),
            ("0123456789", "9876543210", "0A10B"),
            ("0000", "1111", "0A0B"),
            ("1234567890", "1234567890", "10A0B"),
            ("1122", "2211", "0A4B"),
            ("1122", "1221", "2A2B"),
            ("1122", "0000", "0A0B"),
            ("0011223344", "0123456789", "1A4B"),
            ("99999999", "99999099", "7A0B"),
            ("5555", "5555", "4A0B"),
            ("2962", "9262", "2A2B"),
            ("260", "181", "0A0B"),
            ("908", "301", "1A0B"),
        ],
    )
    def test_get_hint(self, secret: str, guess: str, expected: str):
        result = run_get_hint(Solution, secret, guess)
        assert_get_hint(result, expected)
