class Solution:
    # Time: O(n) — each character enters and leaves the window once
    # Space: O(k) — counter holds at most k + 1 distinct characters
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        counts: dict[str, int] = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            while len(counts) > k:
                left_ch = s[left]
                counts[left_ch] -= 1
                if counts[left_ch] == 0:
                    del counts[left_ch]
                left += 1
            best = max(best, right - left + 1)
        return best
