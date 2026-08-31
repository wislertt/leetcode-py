class Solution:
    # Time: O(n)
    # Space: O(1)
    def check_record(self, n: int) -> int:
        mod = 1_000_000_007
        # dp[a][l]: records ending with `a` total absences and `l` trailing
        # consecutive lates.
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            no_absent = sum(dp[0]) % mod
            with_absent = sum(dp[1]) % mod
            nxt = [
                # append 'P' (late streak resets); 'A' starts the streak anew
                [no_absent, dp[0][0], dp[0][1]],
                [(no_absent + with_absent) % mod, dp[1][0], dp[1][1]],
            ]
            dp = nxt
        return (sum(dp[0]) + sum(dp[1])) % mod
