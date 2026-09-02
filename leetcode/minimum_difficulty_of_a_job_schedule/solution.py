from itertools import accumulate


class Solution:
    def min_difficulty(self, job_difficulty: list[int], d: int) -> int:
        n = len(job_difficulty)
        if n < d:
            return -1
        inf = 10**9
        dp = list(accumulate(job_difficulty, max))
        for day in range(1, d):
            ndp = [inf] * n
            for i in range(day, n):
                run_max = 0
                for j in range(i, day - 1, -1):
                    run_max = max(run_max, job_difficulty[j])
                    ndp[i] = min(ndp[i], dp[j - 1] + run_max)
            dp = ndp
        return dp[n - 1]
