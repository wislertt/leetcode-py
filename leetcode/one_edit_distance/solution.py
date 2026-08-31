class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.is_one_edit_distance(t, s)
        if len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1 :] == t[i + 1 :]
                return s[i:] == t[i + 1 :]
        return len(s) + 1 == len(t)
