class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_flips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        # Mismatches of the window starting at index 0 against "0101..." and "1010..."
        mismatch = sum(doubled[i] != "01"[i & 1] for i in range(n))
        best = min(mismatch, n - mismatch)
        # Slide the rotation start: drop the left char, pick up the one entering the window
        for start in range(1, n):
            left = start - 1
            mismatch -= doubled[left] != "01"[left & 1]
            right = start + n - 1
            mismatch += doubled[right] != "01"[right & 1]
            best = min(best, mismatch, n - mismatch)
        return best
