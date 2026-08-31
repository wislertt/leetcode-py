class Solution:
    # Time: O(n)
    # Space: O(k) where k is the alphabet size
    def is_isomorphic(self, s: str, t: str) -> bool:
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}
        for cs, ct in zip(s, t, strict=True):
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True
