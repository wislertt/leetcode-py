class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def sort_array(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sort_array(nums[:mid])
        right = self.sort_array(nums[mid:])

        merged: list[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
