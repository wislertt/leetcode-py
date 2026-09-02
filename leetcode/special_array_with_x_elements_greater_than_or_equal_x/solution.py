class Solution:
    # Time: O(n + m) where m = max(nums)
    # Space: O(m)
    def special_array(self, nums: list[int]) -> int:
        n = len(nums)
        counts = [0] * (n + 1)
        for num in nums:
            counts[min(num, n)] += 1
        total = 0
        for x in range(n, -1, -1):
            total += counts[x]
            if total == x:
                return x
        return -1
