from itertools import product


class Solution:
    # Time: O(n * m * log(n * m))
    # Space: O(n * m)
    def assign_bikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        n, m = len(workers), len(bikes)
        pairs = sorted(
            (abs(w[0] - b[0]) + abs(w[1] - b[1]), i, j)
            for (i, w), (j, b) in product(enumerate(workers), enumerate(bikes))
        )
        used_workers = [False] * n
        used_bikes = [False] * m
        ans = [0] * n
        for _, i, j in pairs:
            if not used_workers[i] and not used_bikes[j]:
                used_workers[i] = used_bikes[j] = True
                ans[i] = j
        return ans
