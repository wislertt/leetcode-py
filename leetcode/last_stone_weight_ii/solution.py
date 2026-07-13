class Solution:
    # Time: O(n * total)
    # Space: O(total)
    def last_stone_weight_ii(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2

        # reachable[s] = True if a subset sums to s.
        reachable = [False] * (target + 1)
        reachable[0] = True

        for stone in stones:
            for s in range(target, stone - 1, -1):
                if reachable[s - stone]:
                    reachable[s] = True

        for s in range(target, -1, -1):
            if reachable[s]:
                return total - 2 * s
        return total
