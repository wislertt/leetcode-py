class Solution:
    # Time: O(n)
    # Space: O(n) for the output
    def di_string_match(self, s: str) -> list[int]:
        low, high = 0, len(s)
        perm: list[int] = []
        for char in s:
            if char == "I":
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
        perm.append(low)
        return perm
