class Solution:
    # Time: O(n)
    # Space: O(1) (at most 32 distinct masks)
    def find_the_longest_substring(self, s: str) -> int:
        # Prefix XOR bitmask over the 5 vowels; two equal prefix masks
        # bracket a substring with all-even vowel counts.
        first_seen = {0: -1}
        mask = 0
        best = 0
        for i, ch in enumerate(s):
            if ch == "a":
                mask ^= 1
            elif ch == "e":
                mask ^= 2
            elif ch == "i":
                mask ^= 4
            elif ch == "o":
                mask ^= 8
            elif ch == "u":
                mask ^= 16
            if mask in first_seen:
                best = max(best, i - first_seen[mask])
            else:
                first_seen[mask] = i
        return best
