class Solution:
    # Time: O(n)
    # Space: O(n)
    def rearrange_array(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
        return result
