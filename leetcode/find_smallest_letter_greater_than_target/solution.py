class Solution:
    # Time: O(log n)
    # Space: O(1)
    def next_greatest_letter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]
