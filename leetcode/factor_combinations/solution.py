class Solution:
    # Time: O(sqrt(n)^d) where d is the max factorization depth
    # Space: O(d)
    def get_factors(self, n: int) -> list[list[int]]:
        results: list[list[int]] = []
        path: list[int] = []

        def dfs(remaining: int, start: int) -> None:
            if path:
                results.append([*path, remaining])
            for factor in range(start, int(remaining**0.5) + 1):
                if remaining % factor == 0:
                    path.append(factor)
                    dfs(remaining // factor, factor)
                    path.pop()

        dfs(n, 2)
        return results
