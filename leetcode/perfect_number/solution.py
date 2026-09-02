class Solution:
    # Time: O(sqrt(n))
    # Space: O(1)
    def check_perfect_number(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                paired = num // i
                if paired != i:
                    total += paired
            i += 1
        return total == num
