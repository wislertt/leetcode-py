from bisect import bisect_left


class Solution:
    # Time: O(n log P + P log log P) where P = max(nums)
    # Space: O(P)
    def prime_sub_operation(self, nums: list[int]) -> bool:
        limit = max(nums)
        sieve = [True] * (limit + 1)
        if limit >= 0:
            sieve[0] = False
        if limit >= 1:
            sieve[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, limit + 1, i):
                    sieve[multiple] = False
        primes = [i for i in range(2, limit + 1) if sieve[i]]

        prev = 0
        for num in nums:
            # Largest prime p < num - prev keeps the resulting value as small as
            # possible while still exceeding prev; a smaller value is never worse.
            idx = bisect_left(primes, num - prev) - 1
            value = num - primes[idx] if idx >= 0 else num
            if value <= prev:
                return False
            prev = value
        return True
