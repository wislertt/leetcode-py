class Solution:
    # Time: O(right * log(log(right)))
    # Space: O(right)
    def closest_primes(self, left: int, right: int) -> list[int]:
        if right < 2:
            return [-1, -1]
        sieve = bytearray([1]) * (right + 1)
        sieve[0] = sieve[1] = 0
        i = 2
        while i * i <= right:
            if sieve[i]:
                sieve[i * i : right + 1 : i] = bytearray(len(sieve[i * i : right + 1 : i]))
            i += 1
        best: list[int] = [-1, -1]
        prev = -1
        for num in range(max(left, 2), right + 1):
            if not sieve[num]:
                continue
            if prev != -1 and (best[0] == -1 or num - prev < best[1] - best[0]):
                best = [prev, num]
            prev = num
        return best
