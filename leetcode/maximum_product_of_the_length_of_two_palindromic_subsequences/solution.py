class Solution:
    # Time: O(2^n * n + 3^n) with n = len(s)
    # Space: O(2^n)
    def max_product(self, s: str) -> int:
        n = len(s)

        def is_palindrome(mask: int) -> bool:
            chars = [s[i] for i in range(n) if mask >> i & 1]
            return chars == chars[::-1]

        length = [0] * (1 << n)
        palindromes: list[int] = []
        for mask in range(1, 1 << n):
            if is_palindrome(mask):
                length[mask] = mask.bit_count()
                palindromes.append(mask)

        best = 0
        for a in palindromes:
            if length[a] * length[a] <= best:
                continue
            remaining = ((1 << n) - 1) ^ a
            # enumerate all submasks of the complement of a
            sub = remaining
            while sub:
                if length[sub]:
                    best = max(best, length[a] * length[sub])
                sub = (sub - 1) & remaining
        return best
