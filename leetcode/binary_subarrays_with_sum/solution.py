class Solution:
    # Time: O(n)
    # Space: O(n)
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        # Prefix sum counts: sum -> number of prefixes with that sum
        prefix_counts: dict[int, int] = {0: 1}
        total = 0
        count = 0
        for num in nums:
            total += num
            count += prefix_counts.get(total - goal, 0)
            prefix_counts[total] = prefix_counts.get(total, 0) + 1
        return count
