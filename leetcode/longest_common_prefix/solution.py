class Solution:
    # Time: O(S) where S is total characters across all strings
    # Space: O(1)
    def longest_common_prefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Vertical scan: compare each character index against all strings
        first = strs[0]
        for i, char in enumerate(first):
            for other in strs[1:]:
                # Stop when index exceeds a string's length or chars mismatch
                if i >= len(other) or other[i] != char:
                    return first[:i]

        return first
