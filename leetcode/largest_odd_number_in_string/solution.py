class Solution:
    # Time: O(n)
    # Space: O(1)
    def largest_odd_number(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[: i + 1]
        return ""
