class Solution:
    # Time: O(n * L) where L is the length of the resulting string
    # Space: O(L)
    def count_and_say(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            parts: list[str] = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                parts.append(str(j - i))
                parts.append(s[i])
                i = j
            s = "".join(parts)
        return s
