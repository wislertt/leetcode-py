class Solution:
    # Time: O(C(9, k) * k)
    # Space: O(k) recursion depth (output excluded)
    def combination_sum_3(self, k: int, n: int) -> list[list[int]]:
        results: list[list[int]] = []
        combo: list[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if len(combo) == k:
                if remaining == 0:
                    results.append([*combo])
                return
            for num in range(start, 10):
                if num > remaining:
                    break
                combo.append(num)
                backtrack(num + 1, remaining - num)
                combo.pop()

        backtrack(1, n)
        return results
