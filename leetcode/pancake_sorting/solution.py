class Solution:
    # Time: O(n^2)
    # Space: O(n) for the working copy
    def pancake_sort(self, arr: list[int]) -> list[int]:
        result: list[int] = []
        work = list(arr)
        for target in range(len(work), 1, -1):
            idx = work.index(target)
            if idx == target - 1:
                continue
            if idx != 0:
                result.append(idx + 1)
                work[: idx + 1] = work[idx::-1]
            result.append(target)
            work[:target] = work[target - 1 :: -1]
        return result
