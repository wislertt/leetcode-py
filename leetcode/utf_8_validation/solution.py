class Solution:
    # Time: O(n)
    # Space: O(1)
    def valid_utf8(self, data: list[int]) -> bool:
        remaining = 0
        for byte in data:
            if remaining == 0:
                if byte >> 7 == 0b0:
                    remaining = 0
                elif byte >> 5 == 0b110:
                    remaining = 1
                elif byte >> 4 == 0b1110:
                    remaining = 2
                elif byte >> 3 == 0b11110:
                    remaining = 3
                else:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                remaining -= 1
        return remaining == 0
