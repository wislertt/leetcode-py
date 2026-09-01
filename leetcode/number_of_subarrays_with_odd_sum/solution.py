class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_of_subarrays(self, arr: list[int]) -> int:
        mod = 1_000_000_007
        result = 0
        odd_prefixes = 0
        even_prefixes = 1  # empty prefix has even sum
        parity = 0
        for value in arr:
            parity ^= value & 1
            if parity:
                result += even_prefixes
                odd_prefixes += 1
            else:
                result += odd_prefixes
                even_prefixes += 1
        return result % mod
