class Solution:
    # Time: O(?)
    # Space: O(?)
    def min_flips_mono_increasing(self, s: str) -> int:
        ones = 0
        flips = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                # Either flip this 0 to 1, or flip all 1s seen so far to 0
                flips = min(flips + 1, ones)
        return flips
