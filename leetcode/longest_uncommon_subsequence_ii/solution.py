class Solution:
    # Time: O(n^2 * (len_i + len_j))
    # Space: O(1)
    def find_lus_length(self, strs: list[str]) -> int:
        # A longest uncommon subsequence, when one exists, can always be taken
        # as one of the input strings in full: any candidate longer than every
        # string it could embed in is already uncommon, so extending it never
        # helps. So scan each string and keep the longest one that is not a
        # subsequence of any other string (duplicates disqualify each other).
        def is_subsequence(short: str, long: str) -> bool:
            if len(short) > len(long):
                return False
            i = 0
            for ch in long:
                if i < len(short) and short[i] == ch:
                    i += 1
            return i == len(short)

        best = -1
        for i, candidate in enumerate(strs):
            if any(
                is_subsequence(candidate, other)
                for j, other in enumerate(strs)
                if i != j and len(other) >= len(candidate)
            ):
                continue
            best = max(best, len(candidate))
        return best
