from functools import cache


class Solution:
    # Time: O(2^m * n * m) where m = len(target), n = len(stickers)
    # Space: O(2^m)
    def min_stickers(self, stickers: list[str], target: str) -> int:
        m = len(target)
        full = (1 << m) - 1
        sticker_counts: list[list[int]] = []
        for sticker in stickers:
            counts = [0] * 26
            for ch in sticker:
                counts[ord(ch) - ord("a")] += 1
            sticker_counts.append(counts)

        @cache
        def dp(mask: int) -> int:
            if mask == full:
                return 0
            # A usable sticker covers at least one letter, so m is an upper bound
            best = m + 1
            for counts in sticker_counts:
                remaining = counts[:]
                new_mask = mask
                for i in range(m):
                    pos = ord(target[i]) - ord("a")
                    if not mask >> i & 1 and remaining[pos]:
                        remaining[pos] -= 1
                        new_mask |= 1 << i
                if new_mask != mask:
                    best = min(best, 1 + dp(new_mask))
            return best

        result = dp(0)
        return result if result <= m else -1
