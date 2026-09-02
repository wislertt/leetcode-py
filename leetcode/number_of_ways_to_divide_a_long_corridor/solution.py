class Solution:
    # Time: O(n)
    # Space: O(1)
    def number_of_ways(self, corridor: str) -> int:
        mod = 1_000_000_007
        seats = 0
        last_pair_end = -1
        ways = 1
        for i, ch in enumerate(corridor):
            if ch != "S":
                continue
            seats += 1
            if seats % 2 == 0:
                last_pair_end = i
            elif seats > 1:
                # divider positions between the previous pair and this new pair
                ways = ways * (i - last_pair_end) % mod
        if seats == 0 or seats % 2:
            return 0
        return ways
