class Solution:
    # Time: O(n) - each index is visited exactly once across all cycles
    # Space: O(1) - marks visited in place, no extra set
    def array_nesting(self, nums: list[int]) -> int:
        best = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            count = 0
            j = i
            while nums[j] >= 0:
                nxt = nums[j]
                nums[j] = -1
                j = nxt
                count += 1
            best = max(best, count)
        return best
