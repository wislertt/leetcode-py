class Solution:
    # Time: O(n) — single pass, O(1) hash lookups
    # Space: O(n) — first-occurrence index per prefix sum
    def max_sub_array_len(self, nums: list[int], k: int) -> int:
        first_index = {0: -1}
        prefix_sum = 0
        best = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - k in first_index:
                best = max(best, i - first_index[prefix_sum - k])
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i
        return best
