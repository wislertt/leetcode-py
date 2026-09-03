class Solution:
    # Time: O(n)
    # Space: O(n)
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        stuck = {f for f, b in zip(fronts, backs, strict=True) if f == b}
        candidates = [x for x in fronts + backs if x not in stuck]
        return min(candidates, default=0)
