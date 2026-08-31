class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def len_longest_fib_subsequence(self, arr: list[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}
        dp: dict[tuple[int, int], int] = {}
        best = 0
        for j in range(len(arr)):
            for i in range(j):
                need = arr[j] - arr[i]
                if need < arr[i] and need in index:
                    dp[(i, j)] = dp.get((index[need], i), 2) + 1
                    best = max(best, dp[(i, j)])
        return best
