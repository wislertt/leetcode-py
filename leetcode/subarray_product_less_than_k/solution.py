class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_subarray_product_less_than_k(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        left = 0
        count = 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
