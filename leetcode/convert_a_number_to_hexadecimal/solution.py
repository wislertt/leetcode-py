class Solution:
    # Time: O(1) - at most 8 hex digits for a 32-bit integer
    # Space: O(1) - output string holds at most 8 characters
    def to_hex(self, num: int) -> str:
        value = num & 0xFFFFFFFF
        digits = "0123456789abcdef"
        if value == 0:
            return "0"
        out: list[str] = []
        while value:
            out.append(digits[value & 0xF])
            value >>= 4
        return "".join(reversed(out))
