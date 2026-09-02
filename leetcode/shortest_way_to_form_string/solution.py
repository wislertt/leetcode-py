class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def shortest_way(self, source: str, target: str) -> int:
        m, n = len(source), len(target)
        ans = j = 0
        while j < n:
            i, k = 0, j
            while i < m and k < n:
                if source[i] == target[k]:
                    k += 1
                i += 1
            if k == j:
                return -1
            j = k
            ans += 1
        return ans
