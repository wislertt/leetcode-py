class Solution:
    # Time: O(sqrt(n))
    # Space: O(1)
    def consecutive_numbers_sum(self, n: int) -> int:
        count = 0
        k = 1
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
            k += 1
        return count
