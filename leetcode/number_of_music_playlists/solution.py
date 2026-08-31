class Solution:
    # Time: O(goal * n)
    # Space: O(n)
    def num_music_playlists(self, n: int, goal: int, k: int) -> int:
        mod = 1_000_000_007
        # dp[j] = number of playlists of current length with j unique songs
        dp = [0] * (n + 1)
        dp[0] = 1
        for _ in range(goal):
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                # Play a new song: choose 1 of the (n - (j - 1)) unused songs
                new_dp[j] = dp[j - 1] * (n - j + 1) % mod
                # Replay a song: any of the j - k previously played songs
                # (a song is replayable once k other songs have been played)
                if j > k:
                    new_dp[j] = (new_dp[j] + dp[j] * (j - k)) % mod
            dp = new_dp
        return dp[n]
