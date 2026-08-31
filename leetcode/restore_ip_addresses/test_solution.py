import pytest

from leetcode_py import logged_test

from .helpers import assert_restore_ip_addresses, run_restore_ip_addresses
from .solution import Solution


class TestRestoreIpAddresses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("25525511135", ["255.255.11.135", "255.255.111.35"]),
            ("0000", ["0.0.0.0"]),
            ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
            ("0", []),
            ("00", []),
            ("000", []),
            ("00000", []),
            ("1111", ["1.1.1.1"]),
            ("1001", ["1.0.0.1"]),
            ("010010", ["0.100.1.0", "0.10.0.10"]),
            ("12345", ["1.2.3.45", "1.2.34.5", "1.23.4.5", "12.3.4.5"]),
            ("255255255255", ["255.255.255.255"]),
            ("255025502550", []),
            ("255255255256", []),
            ("1111111111111", []),
            ("20", []),
        ],
    )
    def test_restore_ip_addresses(self, s: str, expected: list[str]):
        result = run_restore_ip_addresses(Solution, s)
        assert_restore_ip_addresses(result, expected)
