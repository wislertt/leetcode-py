class Solution:
    # Time: O(n * k) where k = len(primes)
    # Space: O(n + k)
    def nth_super_ugly_number(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)
        candidates = list(primes)
        for i in range(1, n):
            nxt = min(candidates)
            ugly[i] = nxt
            for j, prime in enumerate(primes):
                if candidates[j] == nxt:
                    idx[j] += 1
                    candidates[j] = ugly[idx[j]] * prime
        return ugly[n - 1]
