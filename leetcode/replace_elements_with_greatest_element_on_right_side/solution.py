class Solution:
    def replace_elements(self, arr: list[int]) -> list[int]:
        result = [-1] * len(arr)
        best = -1
        for i in range(len(arr) - 1, -1, -1):
            result[i] = best
            best = max(best, arr[i])
        return result
