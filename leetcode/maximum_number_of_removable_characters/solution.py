class Solution:
    # Time: O(len(s) * log(len(removable)))
    # Space: O(len(removable))
    def maximum_removals(self, s: str, p: str, removable: list[int]) -> int:
        def is_subsequence(removed: set[int]) -> bool:
            i = 0
            for j, ch in enumerate(s):
                if i == len(p):
                    return True
                if j in removed or ch != p[i]:
                    continue
                i += 1
            return i == len(p)

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_subsequence(set(removable[:mid])):
                lo = mid
            else:
                hi = mid - 1
        return lo
