class Solution:
    # Time: O(2^n * n)
    # Space: O(n) recursion depth (output excluded)
    def find_subsequences(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            if len(path) >= 2:
                result.append(path.copy())
            seen: set[int] = set()
            for i in range(start, len(nums)):
                if nums[i] in seen or (path and nums[i] < path[-1]):
                    continue
                seen.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
