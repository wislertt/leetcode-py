from itertools import product


class Solution:
    # Time: O(n * k) expansions where k is average option count
    # Space: O(result)
    def expand(self, s: str) -> list[str]:
        blocks: list[list[str]] = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                j = s.index("}", i)
                blocks.append(sorted(s[i + 1 : j].split(",")))
                i = j + 1
            else:
                j = s.find("{", i)
                if j == -1:
                    blocks.append([s[i:]])
                    i = len(s)
                else:
                    blocks.append([s[i:j]])
                    i = j
        return sorted("".join(word) for word in product(*blocks))
