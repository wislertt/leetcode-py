class Solution:
    # Time: O(n)
    # Space: O(1)
    def take_characters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0, 0, 0]
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        if any(c < k for c in count):
            return -1

        # Keep the longest middle window whose removal leaves >= k of each char.
        best = 0
        left = 0
        for right, ch in enumerate(s):
            count[ord(ch) - ord("a")] -= 1
            while count[ord(ch) - ord("a")] < k:
                count[ord(s[left]) - ord("a")] += 1
                left += 1
            best = max(best, right - left + 1)
        return n - best
