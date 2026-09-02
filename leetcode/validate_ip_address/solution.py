class Solution:
    # Time: O(n)
    # Space: O(n) for the split parts
    def valid_ip_address(self, query_ip: str) -> str:
        if self._is_ipv4(query_ip):
            return "IPv4"
        if self._is_ipv6(query_ip):
            return "IPv6"
        return "Neither"

    def _is_ipv4(self, query_ip: str) -> bool:
        parts = query_ip.split(".")
        if len(parts) != 4:
            return False
        return all(self._is_ipv4_octet(part) for part in parts)

    def _is_ipv4_octet(self, part: str) -> bool:
        if not part or len(part) > 3 or not part.isdigit():
            return False
        if part[0] == "0" and len(part) > 1:
            return False
        return int(part) <= 255

    def _is_ipv6(self, query_ip: str) -> bool:
        parts = query_ip.split(":")
        if len(parts) != 8:
            return False
        return all(self._is_ipv6_group(part) for part in parts)

    def _is_ipv6_group(self, part: str) -> bool:
        if not 1 <= len(part) <= 4:
            return False
        return all(char in self.HEX_DIGITS for char in part)

    HEX_DIGITS: frozenset[str] = frozenset("0123456789abcdefABCDEF")
