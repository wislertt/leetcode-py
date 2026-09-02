class Solution:
    # Time: O(log n)
    # Space: O(1)
    def last_remaining(self, n: int) -> int:
        head, step, left = 1, 1, True
        while n > 1:
            if left or n % 2 == 1:
                head += step
            step *= 2
            n //= 2
            left = not left
        return head
