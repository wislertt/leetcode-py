class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def can_cross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False
        positions = set(stones)
        last = stones[-1]
        if last == 1:
            return True
        jumps: dict[int, set[int]] = {pos: set() for pos in stones}
        jumps[1].add(1)
        for pos in stones[1:]:
            for k in jumps[pos]:
                for step in (k - 1, k, k + 1):
                    nxt = pos + step
                    if step > 0 and nxt in positions:
                        if nxt == last:
                            return True
                        jumps[nxt].add(step)
        return False
