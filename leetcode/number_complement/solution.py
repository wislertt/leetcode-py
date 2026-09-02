class Solution:
    # Time: O(log num)
    # Space: O(1)
    def find_complement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
