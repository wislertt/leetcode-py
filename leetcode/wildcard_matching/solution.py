class Solution:
    # Time: O(s_len * p_len) worst case (star backtracking), Space: O(1)
    def is_match(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        i = j = 0
        star_idx = -1
        match_idx = 0
        while i < s_len:
            if j < p_len and (p[j] == "?" or p[j] == s[i]):
                i += 1
                j += 1
            elif j < p_len and p[j] == "*":
                star_idx = j
                match_idx = i
                j += 1
            elif star_idx >= 0:
                j = star_idx + 1
                match_idx += 1
                i = match_idx
            else:
                return False
        while j < p_len and p[j] == "*":
            j += 1
        return j == p_len
