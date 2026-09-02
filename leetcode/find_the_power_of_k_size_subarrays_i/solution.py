class Solution:
    # Time: O(n)
    # Space: O(1) extra (output excluded)
    def results_array(self, nums: list[int], k: int) -> list[int]:
        # run[i] = length of the consecutive ascending run ending at index i
        results: list[int] = []
        run = 1
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1] + 1:
                run += 1
            else:
                run = 1
            if i >= k - 1:
                results.append(num if run >= k else -1)
        return results
