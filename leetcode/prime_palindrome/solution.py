class Solution:
    # Time: O(sqrt(m) * log(m)) over the palindrome candidates up to the answer m
    # Space: O(1)
    def prime_palindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        for x in (2, 3, 5, 7, 11):
            if x >= n:
                return x
        # Every palindrome with an even number of digits is divisible by 11,
        # so 11 above is the only even-length prime palindrome. Walk the
        # odd-length ones by mirroring their first half.
        for length in (3, 5, 7, 9):
            half = 10 ** (length // 2)
            for root in range(half, half * 10):
                s = str(root)
                candidate = int(s + s[-2::-1])
                if candidate >= n and is_prime(candidate):
                    return candidate
        raise ValueError(f"no prime palindrome at or above {n}")
