class Solution:
    # Time: O(log_3 n)
    # Space: O(1)
    def check_powers_of_three(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
