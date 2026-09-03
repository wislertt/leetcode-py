class Solution:
    # Time: O(log n)
    # Space: O(1)
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
