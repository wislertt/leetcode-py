class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def is_happy(self, n: int) -> bool:
        def digit_square_sum(num: int) -> int:
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow, fast = n, digit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
        return fast == 1
