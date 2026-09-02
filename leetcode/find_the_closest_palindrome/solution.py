class Solution:
    # Time: O(len(n))
    # Space: O(len(n))
    def nearest_palindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        candidates: set[int] = {10 ** (length - 1) - 1, 10**length + 1}
        prefix = int(n[: (length + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            left = str(p)
            mirrored = left if length % 2 == 0 else left[:-1]
            candidates.add(int(left + mirrored[::-1]))
        candidates.discard(num)
        best: int = candidates.pop()
        for cand in candidates:
            if (abs(cand - num), cand) < (abs(best - num), best):
                best = cand
        return str(best)
