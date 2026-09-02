class Solution:
    # Time: O(log k)
    # Space: O(log k)
    def find_kth_bit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        half = 1
        while half * 2 + 1 < k:
            half = half * 2 + 1
        mid = half + 1
        if k == mid:
            return "1"
        mirrored = self.find_kth_bit(n, mid - (k - mid))
        return "0" if mirrored == "1" else "1"
