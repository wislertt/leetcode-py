class Solution:
    # Time: O(sqrt(n))
    # Space: O(1)
    def min_steps(self, n: int) -> int:
        # Each run of pastes multiplies the screen by a factor; copying a
        # block of size d costs d operations total, so the answer is the sum
        # of the prime factors of n.
        operations = 0
        factor = 2
        while factor * factor <= n:
            while n % factor == 0:
                operations += factor
                n //= factor
            factor += 1
        if n > 1:
            operations += n
        return operations
