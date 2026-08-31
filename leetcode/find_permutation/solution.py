class Solution:
    # Time: O(n)
    # Space: O(1) extra (output excluded)
    def find_permutation(self, s: str) -> list[int]:
        n = len(s) + 1
        perm = list(range(1, n + 1))
        i = 0
        while i < len(s):
            if s[i] == "D":
                j = i
                while j < len(s) and s[j] == "D":
                    j += 1
                perm[i : j + 1] = perm[i : j + 1][::-1]
                i = j
            else:
                i += 1
        return perm
