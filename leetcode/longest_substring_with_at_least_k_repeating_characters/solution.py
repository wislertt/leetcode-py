class Solution:
    # Time: O(26 * n) -> O(n)
    # Space: O(26) -> O(1)
    def longest_substring_with_at_least_k_repeating_characters(self, s: str, k: int) -> int:
        best = 0
        for target in range(1, 27):
            if target * k > len(s):
                break
            counts: dict[str, int] = {}
            left = 0
            for right, ch in enumerate(s):
                counts[ch] = counts.get(ch, 0) + 1
                while len(counts) > target:
                    counts[s[left]] -= 1
                    if counts[s[left]] == 0:
                        del counts[s[left]]
                    left += 1
                if len(counts) == target and all(c >= k for c in counts.values()):
                    best = max(best, right - left + 1)
        return best
