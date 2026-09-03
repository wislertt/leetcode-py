class Solution:
    # Time: O(n)
    # Space: O(1)
    def can_transform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False
        if start.replace("X", "") != result.replace("X", ""):
            return False
        i = 0
        j = 0
        n = len(start)
        while i < n and j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1
            if i == n or j == n:
                break
            if start[i] != result[j]:
                return False
            # 'L' can only move left, 'R' can only move right
            if (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False
            i += 1
            j += 1
        return True
