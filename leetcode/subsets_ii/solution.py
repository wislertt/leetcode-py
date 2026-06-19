class Solution:
    # Time: O(n * 2^n)
    # Space: O(n) recursion stack
    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = []
        subset: list[int] = []

        def backtrack(start: int) -> None:
            result.append(list(subset))
            for i in range(start, len(nums)):
                # Skip duplicates at the same depth to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result
