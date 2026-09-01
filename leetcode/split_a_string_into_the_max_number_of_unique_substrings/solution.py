class Solution:
    # Time: O(n * 2^n) worst case, pruned hard by the remaining-suffix bound
    # Space: O(n) recursion depth plus the seen-set of at most n pieces
    def max_unique_split(self, s: str) -> int:
        n = len(s)
        seen: set[str] = set()

        def dfs(start: int, count: int) -> int:
            best = count
            for end in range(start + 1, n + 1):
                piece = s[start:end]
                # Even taking every remaining character as its own split cannot
                # beat the best found so far.
                if piece in seen or count + 1 + (n - end) <= best:
                    continue
                seen.add(piece)
                best = max(best, dfs(end, count + 1))
                seen.remove(piece)
            return best

        return dfs(0, 0)
