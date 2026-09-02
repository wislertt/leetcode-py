class Solution:
    # Time: O(m + n * L) where m is total mapping size, L the average substituted length
    # Space: O(m + n * L)
    def apply_substitutions(self, replacements: list[list[str]], text: str) -> str:
        values: dict[str, str] = dict(replacements)

        def dfs(s: str) -> str:
            i = s.find("%")
            if i == -1:
                return s
            j = s.find("%", i + 1)
            if j == -1:
                return s
            key = s[i + 1 : j]
            return s[:i] + dfs(values[key]) + dfs(s[j + 1 :])

        return dfs(text)
