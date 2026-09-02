class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_swaps(self, s: str) -> int:
        unmatched_close = 0
        max_unmatched_close = 0
        for ch in s:
            if ch == "]":
                unmatched_close += 1
                max_unmatched_close = max(max_unmatched_close, unmatched_close)
            else:
                unmatched_close -= 1
        return (max_unmatched_close + 1) // 2
