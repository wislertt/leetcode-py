class Solution:
    # Time: O(2^n)
    # Space: O(n)
    def combination_sum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result: list[list[int]] = []

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
