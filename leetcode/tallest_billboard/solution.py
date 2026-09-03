class Solution:
    # Time: O(n * diff) where diff <= sum(rods)
    # Space: O(diff)
    def tallest_billboard(self, rods: list[int]) -> int:
        # dp[d] = largest total height of the taller support when the
        # two supports differ by exactly d (d >= 0).
        dp: dict[int, int] = {0: 0}
        for rod in rods:
            nxt = dict(dp)
            for diff, taller in dp.items():
                # put the rod on the taller support
                nxt[diff + rod] = max(nxt.get(diff + rod, 0), taller + rod)
                # put the rod on the shorter support
                if rod >= diff:
                    nxt[rod - diff] = max(nxt.get(rod - diff, 0), taller - diff + rod)
                else:
                    nxt[diff - rod] = max(nxt.get(diff - rod, 0), taller)
            dp = nxt
        return dp.get(0, 0)
