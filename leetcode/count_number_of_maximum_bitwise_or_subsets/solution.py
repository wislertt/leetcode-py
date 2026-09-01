class Solution:
    # Time: O(n * max_or) where max_or <= 2^17 for nums[i] <= 10^5
    # Space: O(max_or)
    def count_max_or_subsets(self, nums: list[int]) -> int:
        target = 0
        for num in nums:
            target |= num
        # counts[acc] = number of subsets (possibly empty) with OR value acc
        counts = [1] + [0] * target
        for num in nums:
            for acc in range(target, -1, -1):
                if counts[acc]:
                    counts[acc | num] += counts[acc]
        return counts[target]
