class Solution:
    # Time: O(total length^2) worst case from cut-point candidates
    # Space: O(total length)
    def split_looping_string(self, strs: list[str]) -> str:
        n = len(strs)
        best_parts = [max(s, s[::-1]) for s in strs]
        best = ""
        for i in range(n):
            left = "".join(best_parts[:i])
            right = "".join(best_parts[i + 1 :])
            for t in (strs[i], strs[i][::-1]):
                for k in range(len(t)):
                    cand = t[k:] + right + left + t[:k]
                    if cand > best:
                        best = cand
        return best
