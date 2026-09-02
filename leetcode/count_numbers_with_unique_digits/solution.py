class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_numbers_with_unique_digits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 10
        count = 9
        available = 9
        for _ in range(2, n + 1):
            count *= available
            available -= 1
            total += count
        return total
