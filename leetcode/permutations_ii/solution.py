class Solution:
    # Time: O(n * n!)
    # Space: O(n)
    def permute_unique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = []
        used = [False] * len(nums)

        def backtrack(current: list[int]) -> None:
            if len(current) == len(nums):
                result.append(list(current))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result
