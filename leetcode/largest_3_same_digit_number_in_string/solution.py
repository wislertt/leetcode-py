class Solution:
    # Time: O(n)
    # Space: O(1)
    def largest_good_integer(self, num: str) -> str:
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2] and num[i] * 3 > best:
                best = num[i] * 3
        return best
