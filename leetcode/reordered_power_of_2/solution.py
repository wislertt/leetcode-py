class Solution:
    # Time: O(d log d) where d is the number of digits in n
    # Space: O(d)
    def reordered_power_of_2(self, n: int) -> bool:
        digits = sorted(str(n))
        return any(sorted(str(1 << k)) == digits for k in range(31))
