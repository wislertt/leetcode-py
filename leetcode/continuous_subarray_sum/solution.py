class Solution:
    # Time: O(n)
    # Space: O(min(n, k))
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        remainder_index: dict[int, int] = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix = (prefix + num) % k
            if prefix in remainder_index:
                if i - remainder_index[prefix] >= 2:
                    return True
            else:
                remainder_index[prefix] = i
        return False
