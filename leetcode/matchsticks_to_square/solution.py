class Solution:
    # Time: O(4^n) backtracking in the worst case (pruned heavily in practice)
    # Space: O(n) recursion stack
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        # Sort descending so larger sticks fail fast and prune the search early.
        sticks = sorted(matchsticks, reverse=True)
        if sticks[0] > side:
            return False
        sides = [0, 0, 0, 0]

        def backtrack(index: int) -> bool:
            if index == len(sticks):
                return all(s == side for s in sides)
            stick = sticks[index]
            for i in range(4):
                if sides[i] + stick > side:
                    continue
                # Skip duplicate side fills to avoid symmetric permutations.
                if i > 0 and sides[i] == sides[i - 1]:
                    continue
                sides[i] += stick
                if backtrack(index + 1):
                    return True
                sides[i] -= stick
            return False

        return backtrack(0)
