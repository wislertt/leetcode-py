class Solution:
    # Time: O(n log log n)
    # Space: O(n)
    def count_primes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = False
        return sum(is_prime)
