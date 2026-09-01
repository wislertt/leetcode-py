class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_vowels(self, s: str, k: int) -> int:
        vowels = frozenset("aeiou")
        count = sum(c in vowels for c in s[:k])
        best = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            if count > best:
                best = count
                if best == k:
                    return best
        return best
