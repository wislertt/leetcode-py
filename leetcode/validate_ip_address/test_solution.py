import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_ip_address, run_valid_ip_address
from .solution import Solution


class TestValidIpAddress:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "query_ip, expected",
        [
            ("172.16.254.1", "IPv4"),
            ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
            ("256.256.256.256", "Neither"),
            ("192.168.1.0", "IPv4"),
            ("192.168.01.1", "Neither"),
            ("192.168.1.00", "Neither"),
            ("192.168.1.1a", "Neither"),
            ("2001:0db8:85a3::8A2E:037j:7334", "Neither"),
            ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", "Neither"),
            ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
            ("1.1.1.1", "IPv4"),
            ("255.255.255.255", "IPv4"),
            ("0.0.0.0", "IPv4"),
            ("1.0.1.", "Neither"),
            ("12.34.56", "Neither"),
            ("12..33.4", "Neither"),
            ("1e1.4.5.6", "Neither"),
            ("1.2.3.4.5", "Neither"),
            ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
            ("20EE:FGb8:85a3:0:0:8A2E:0370:7334", "Neither"),
            ("2001:db8:85a3:0:0:8A2E:0370:7334:0", "Neither"),
            ("1:2:3:4:5:6:7::", "Neither"),
            ("12345:2:3:4:5:6:7:8", "Neither"),
            ("a", "Neither"),
            ("", "Neither"),
        ],
    )
    def test_valid_ip_address(self, query_ip: str, expected: str):
        result = run_valid_ip_address(Solution, query_ip)
        assert_valid_ip_address(result, expected)
