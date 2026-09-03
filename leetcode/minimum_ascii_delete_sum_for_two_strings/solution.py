class Solution:
    # Time: O(m * n)
    # Space: O(min(m, n))
    def minimum_delete_sum(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        prev = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            prev[j] = prev[j - 1] + ord(s2[j - 1])
        for i in range(1, len(s1) + 1):
            curr = [prev[0] + ord(s1[i - 1])]
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr.append(prev[j - 1])
                else:
                    curr.append(min(prev[j] + ord(s1[i - 1]), curr[j - 1] + ord(s2[j - 1])))
            prev = curr
        return prev[-1]
