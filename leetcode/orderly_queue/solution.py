class Solution:
    # Time: O(n^2) for k == 1 (n rotations of length n), O(n log n) for k >= 2
    # Space: O(n) for the rotation candidates
    def orderly_queue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return "".join(sorted(s))
