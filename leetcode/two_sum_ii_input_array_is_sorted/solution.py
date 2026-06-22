class Solution:
    # Time: O(n)
    # Space: O(1)
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            if current < target:
                left += 1
            else:
                right -= 1
        return []
