class Solution:
    # Time: O(n * 10)
    # Space: O(1)
    def knight_dialer(self, n: int) -> int:
        mod = 1_000_000_007
        moves: dict[int, tuple[int, ...]] = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
        }
        # dp[digit] = number of distinct numbers of current length ending here
        dp = [1] * 10
        for _ in range(n - 1):
            new_dp = [0] * 10
            for digit in range(10):
                for nxt in moves[digit]:
                    new_dp[nxt] = (new_dp[nxt] + dp[digit]) % mod
            dp = new_dp
        return sum(dp) % mod
