class Solution:
    # Time: O(n)
    # Space: O(1) excluding output
    def large_group_positions(self, s: str) -> list[list[int]]:
        result: list[list[int]] = []
        start = 0
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i
        return result
