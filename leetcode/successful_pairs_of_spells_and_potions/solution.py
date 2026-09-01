class Solution:
    # Time: O((n + m) log m) - sorting potions plus a binary search per spell
    # Space: O(m) - sorted copy of the potions
    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(potions)
        pairs: list[int] = []
        for spell in spells:
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) // 2
                if spell * potions[mid] >= success:
                    hi = mid
                else:
                    lo = mid + 1
            pairs.append(n - lo)
        return pairs
