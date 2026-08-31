class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_strobogrammatic(self, num: str) -> bool:
        rotated = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in rotated or rotated[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
